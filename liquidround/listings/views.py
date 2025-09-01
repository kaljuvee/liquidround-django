import json
import datetime 
from django.utils import timezone
from django.http import Http404, HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.utils.text import slugify
# Create your views here.
from django.views import generic

from . import models
from . import forms
from companies.models import Company, Industry
from statpages import mixins as statpages_mixins
from accounts.mixins import RequestKwargToForm
from accounts.models import Notification

class CreateListing(statpages_mixins.TopMenu,
                    RequestKwargToForm,
                    generic.edit.FormView):
    template_name = 'listings/create_listing.html'
    form_class = forms.ListingForm

    def get_context_data(self, *args, **kwargs):
        context = super(CreateListing, self).get_context_data(*args, **kwargs)
        context['industries'] = Industry.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('listing:success', args=[self.kwargs['listing_type']])

    def get_initial(self):
        initial = super(CreateListing, self).get_initial()
        initial['listing_type'] = self.kwargs['listing_type']

        company_slug = self.request.GET.get('company', None)
        if company_slug is not None:
            try:
                company = Company.objects.get(slug=company_slug)
                initial['company_id'] = company.id
                initial['company'] = company.title
            except:
                pass

        return initial

    def form_valid(self, form):
        clean = form.cleaned_data

        company = Company.objects.filter(title__iexact=clean['company'])
        try:
            company = company[0]
        except:
            company = Company.objects.create(
                    title=clean['company'],
                    slug=slugify(clean['company']),
                    industry_id=clean['industry'],
                    website=clean['website'],
                    role=clean['specificrole']
                )


        listing = models.Listing(
            user=self.request.user.profile,
            company=company,
            shares=clean['shares'],
            price=clean['price'],
            listing_type=clean['listing_type']
        )
        listing.save()

        watchers = company.watching.all()
        if len(watchers) > 0:
            notifications = []
            for w in watchers:
                notifications.append(Notification(user=w, company=company, listing=listing))
            if len(notifications) > 0:
                Notification.objects.bulk_create(notifications)


        return super(CreateListing, self).form_valid(form)


class Created(statpages_mixins.TopMenu, generic.TemplateView):

    def get_template_names(self):
        return['listings/thanks_%s.html' % self.kwargs['listing_type']]


class MarkAs(generic.View):

    mark = 'deleted'

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            if request.user.is_authenticated():
                result = {'success': False}
                listing_id = request.POST.get('id',None)

                if listing_id:
                    try:
                        listing = models.Listing.objects.get(pk=listing_id)
                    except:
                        raise Http404

                    if listing.user.user == request.user or request.user.is_staff:
                        if self.mark == 'deleted':
                            listing.is_deleted = True
                            listing.save()
                            result['success'] = True
                        elif self.mark == 'closed':
                            listing.is_closed = True
                            listing.closedon = timezone.now()
                            listing.save()
                            result['success'] = True
                            result['listing'] = listing.history_dict()

                        return HttpResponse(json.dumps(result), content_type='application/json')
        raise Http404

class Prolong(statpages_mixins.TopMenu, generic.TemplateView):
    template_name = 'listings/prolong_success.html'

    def get_context_data(self, **kwargs):
        context = super(Prolong, self).get_context_data(**kwargs)

        try:
            code = self.kwargs['code']
            listing = models.Listing.objects.get(prolong_code=code)
        except:
            raise Http404

        listing.prolong_code = ''
        listing.prolong_messaged = False
        listing.expireson = datetime.datetime.now() + datetime.timedelta(days=60)
        listing.save()

        return context