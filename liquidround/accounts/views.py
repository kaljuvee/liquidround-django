import hashlib
import datetime

from django.shortcuts import render, redirect
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import ListView

from django.db.models import IntegerField, Sum, Case, When, Q, Value

from django.contrib.auth import authenticate, login, logout
# Create your views here.
from django.contrib.auth.models import User
from . import forms
from . import mixins
from . import models
from companies.models import Company
from statpages import mixins as statpages_mixins


class Register(statpages_mixins.TopMenu,
               mixins.RequestKwargToForm, 
               generic.edit.FormView):
    template_name = 'accounts/register.html'
    form_class = forms.RegisterForm
    success_url = reverse_lazy('accounts:thanks')

    def form_valid(self, form):
        username = form.cleaned_data['email'] \
                    .replace('@','_') \
                    .replace('.','-')
        # check for existence was in form method
        user = User.objects.create_user(
                username,
                form.cleaned_data['email'],
                form.cleaned_data['password']
                )

        code = hashlib.md5(str(user.username) + str(form.cleaned_data['password']) + str(datetime.datetime.now())).hexdigest()
        p = models.Profile(
            user=user,
            phone=form.cleaned_data['phone'],
            certified=form.cleaned_data['certified'],
            activationcode=code
        )

        user.is_active = False

        names = form.cleaned_data['full_name'].split(" ")
        if len(names) > 1:
            user.first_name = names[0]
            user.last_name = " ".join(names[1:])
        else:
            user.first_name = form.cleaned_data['full_name']
        p.save()
        user.save()
        form.mail(code) # sends email with activate

        return super(Register, self).form_valid(form)

class RegisterThanks(statpages_mixins.TopMenu, TemplateView):
    template_name = 'accounts/thanks.html'

class RegisterActivation(statpages_mixins.TopMenu,TemplateView):
    template_name = 'accounts/activate_status.html'

    def get_context_data(self, **kwargs):
        context = super(RegisterActivation, self).get_context_data(**kwargs)
        print kwargs['code']
        try:
            user = models.Profile.objects.get(activationcode=kwargs['code'])
        except:
            raise Http404
        user.activationcode = ''
        user.activatedon = datetime.datetime.now()
        user.user.is_active = True
        user.user.save()
        user.save()
        return context

class Profile(statpages_mixins.TopMenu, DetailView):
    model = models.Profile
    template_name = 'accounts/profile.html'
    context_object_name = 'profile'

    def get_object(self, *args, **kwargs):
        try:
            obj = super(Profile, self).get_object(*args, **kwargs)
        except AttributeError:
            if self.request.user.is_authenticated():
                obj = models.Profile.objects.get(user=self.request.user)
            else:
                raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)

        context['equities'] = self.object.listings.filter(
                is_closed=False,
                listing_type='equity',
                is_deleted=False,
                expireson__gt=datetime.datetime.now()
            )

        context['offers'] = self.object.listings.filter(
                is_closed=False,
                listing_type='offer',
                is_deleted=False,
                expireson__gt=datetime.datetime.now()
            )
        context['sell_history'] = self.object.listings.filter(
                is_closed=True,
                listing_type='equity',
                is_deleted=False
            )
        context['buy_history'] = self.object.listings.filter(
                is_closed=True,
                listing_type='offer',
                is_deleted=False
            )

        watching = self.object.watching.all()

        # notifications = self.object.notifications \
        #     .annotate(
        #         equities_count=Sum(
        #             Case(
        #                 When(
        #                      listing__listing_type='equity',
        #                      listing__is_approved=True,
        #                      listing__is_closed=False,
        #                      then=1,
        #                 ),
        #                 default=Value(0),
        #                 output_field=IntegerField()
        #             )
        #         ),
        #         offers_count=Sum(
        #             Case(
        #                 When(
        #                      listing__listing_type='offer',
        #                      listing__is_approved=True,
        #                      listing__is_closed=False,
        #                      then=1,
        #                 ),
        #                 default=Value(0),
        #                 output_field=IntegerField()
        #             )
        #         )
        #     ).order_by('equities_count','offers_count')
        context['notifications'] = [w.brief_dict(self.request.user.profile) for w in watching]
        context['noti_count'] = 0
        for c in context['notifications']:
            context['noti_count'] += c['offers_count'] + c['equities_count']
        #     print c
        #     for n in notifications:
        #         print "%s=%s" % (n.company.id, c['id'])
        #         if n.company.id == c['id'] and not c.has_key('equities_count'):
        #             context['noti_count'] += 1
        #             c['equities_count'] = n.equities_count
        #             c['offers_count'] = n.offers_count

        

        
        print context['notifications']

        return context

class EditProfile(statpages_mixins.TopMenu, generic.edit.FormView):
    template_name = 'accounts/edit_profile.html'
    form_class = forms.ProfileForm
    success_url = reverse_lazy('accounts:profile')

    def get_initial(self):
        initial = super(EditProfile, self).get_initial()
        initial['phone'] = self.request.user.profile.phone
        return initial

    def form_valid(self, form):
        clean = form.cleaned_data
        self.request.user.profile.phone = clean['phone']
        self.request.user.profile.save()

        return super(EditProfile, self).form_valid(form)


class Signin(statpages_mixins.TopMenu,mixins.RequestKwargToForm, generic.edit.FormView):
    template_name = 'accounts/login.html'
    form_class = forms.LoginForm
    success_url = reverse_lazy('statpages:home')

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = authenticate(
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
        if user is not None:
            if user.is_active:
                login(form.request, user)
                return super(Signin, self).form_valid(form)

        return self.form_invalid(form)

def signoff(request):
    logout(request)
    return redirect(reverse_lazy('statpages:home'))