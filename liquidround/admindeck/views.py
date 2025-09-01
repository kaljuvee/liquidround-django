import json
import datetime

from django.http import Http404, HttpResponse
from django.utils import timezone
from django.core.urlresolvers import reverse_lazy
from django.core.files import File

from django.views import generic
# Create your views here.
from statpages import mixins as statpages_mixins
from accounts import mixins as accounts_mixins
from accounts.models import Profile
from .models import CompanyRequest
from listings import models
from companies.models import Company, Photo, Document
from msgs.models import Message
from listings import forms

class Deck(accounts_mixins.StaffOnly,
           statpages_mixins.TopMenu,
           generic.TemplateView):
    template_name = 'admindeck/deck.html'

    def get_context_data(self, **kwargs):
        context = super(Deck, self).get_context_data(**kwargs)
        context['equities'] = models.Listing.objects.filter(
                is_approved=False,
                is_deleted=False,
                listing_type='equity'
            ).count()

        context['offer'] = models.Listing.objects.filter(
                is_approved=False,
                is_deleted=False,
                listing_type='offer'
            ).count()

        context['users'] = Profile.objects.all().count()
        context['documents'] = Document.objects.all().count()
        context['companyrequests'] = CompanyRequest.objects.filter(done=False).count()

        return context


class Listings(accounts_mixins.StaffOnly,
              statpages_mixins.TopMenu,
              generic.ListView):

    model = models.Listing
    context_object_name = 'listings'
    template_name = 'admindeck/approval.html'
    listing_type = 'equity'

    def get_queryset(self):
        qs = super(Listings, self).get_queryset()
        return qs.filter(listing_type=self.listing_type, is_approved=False, is_deleted=False, is_closed=False)

class Users(accounts_mixins.StaffOnly,
            statpages_mixins.TopMenu,
            generic.ListView):
    model = Profile
    context_object_name = 'users'
    template_name = 'admindeck/users.html'

class Documents(accounts_mixins.StaffOnly,
            statpages_mixins.TopMenu,
            generic.ListView):
    model = Document
    context_object_name = 'documents'
    template_name = 'admindeck/documents.html'


class Statistic(accounts_mixins.StaffOnly,
                statpages_mixins.TopMenu,
                generic.TemplateView):
    template_name = 'admindeck/statistic.html'

    def get_context_data(self, **kwargs):
        context = super(Statistic, self).get_context_data(**kwargs)
        context['users'] = Profile.objects.all().count()
        context['active_users'] = Profile.objects.filter(user__last_login__gte=datetime.datetime.now() - datetime.timedelta(days=60)).count()
        context['unactive_users'] = context['users'] - context['active_users']
        context['company'] = Company.objects.filter(published=True).count()
        context['registrations'] = Profile.objects.filter(
            activatedon__range=(
            datetime.datetime.combine(datetime.date.today(), datetime.time.min),
            datetime.datetime.combine(datetime.date.today(), datetime.time.max),
                )
            ).count()

        listings = models.Listing.objects.filter(createdon__range=(
            datetime.datetime.combine(datetime.date.today(), datetime.time.min),
            datetime.datetime.combine(datetime.date.today(), datetime.time.max),
                )).count()

        context['transactions'] = models.Listing.objects.filter(closedon__range=(
            datetime.datetime.combine(datetime.date.today(), datetime.time.min),
            datetime.datetime.combine(datetime.date.today(), datetime.time.max),
                )).count()

        requests = Message.objects.filter(createdon__range=(
            datetime.datetime.combine(datetime.date.today(), datetime.time.min),
            datetime.datetime.combine(datetime.date.today(), datetime.time.max),
                )).count()

        context['actions'] = listings + requests
        
        return context


class EditListing(accounts_mixins.StaffOnly,
                  statpages_mixins.TopMenu,
                  generic.edit.FormView):

    template_name = 'admindeck/edit_listing.html'
    form_class = forms.EditListing
    success_url = reverse_lazy('admindeck:thanks')

    def get_context_data(self, **kwargs):
        context = super(EditListing, self).get_context_data(**kwargs)
        try:
            listing = models.Listing.objects.get(pk=self.kwargs['listing_id'])
            context['files'] = listing.company.documents.all()
        except:
            pass
        
        
        return context

    def get_initial(self):
        initial = super(EditListing, self).get_initial()
        try:
            listing = models.Listing.objects.get(pk=self.kwargs['listing_id'])
        except:
            raise Http404
        initial['company_id'] = listing.company.id
        initial['published'] = listing.company.published
        initial['company'] = listing.company.title
        initial['industry'] = listing.company.industry
        initial['specificrole'] = listing.company.role
        initial['website'] = listing.company.website
        initial['summary'] = listing.company.summary
        initial['country'] = listing.company.country
        initial['city'] = listing.company.city
        initial['pre_emption_rights'] = listing.company.pre_emption_rights
        initial['voting_rights'] = listing.company.voting_rights
        initial['class_a'] = listing.company.class_a
        initial['class_b'] = listing.company.class_b
        initial['funding_stage'] = listing.company.funding_stage

        initial['listing_type'] = listing.listing_type
        initial['shares'] = listing.shares
        initial['price'] = listing.price

        return initial

    def form_valid(self, form):
        clean = form.cleaned_data
        try:
            listing = models.Listing.objects.get(pk=self.kwargs['listing_id'])
        except:
            raise Http404

        if clean['company_id']:
            listing.company = Company.objects.get(pk=clean['company_id'])
            listing.company.published = clean['published']
            listing.company.industry = clean['industry']
            listing.company.role = clean['specificrole']
            listing.company.city = clean['city']
            listing.company.country = clean['country']
            listing.company.summary = clean['summary']
            listing.company.pre_emption_rights = clean['pre_emption_rights']
            listing.company.voting_rights = clean['voting_rights']
            listing.company.class_a = clean['class_a']
            listing.company.class_b = clean['class_b']
            listing.company.funding_stage = clean['funding_stage']
            listing.company.save()
        else:
            company = Company.objects.create(
                company=clean['company'],
                industry=clean['industry'],
                specificrole=clean['specificrole'],
                website=clean['website'],
                summary=clean['summary'],
                country=clean['country'],
                city=clean['city'],
                pre_emption_rights=clean['pre_emption_rights'],
                voting_rights=clean['voting_rights'],
                class_a=clean['class_a'],
                class_b=clean['class_b'],
                funding_stage=clean['funding_stage']
            )
            listing.company = company

        files = self.request.FILES.getlist('images')
        if len(files) > 0:
            for f in files:
                image = File(f)
                photo = Photo(company=listing.company, image=image)
                photo.save()

        files = self.request.FILES.getlist('docs[]')
        titles = self.request.POST.getlist('title[]')
        if len(files) > 0:
            for i,f in enumerate(files):
                doc = File(f)
                document = Document(company=listing.company, doc=doc, title=titles[i], uploadedby=self.request.user.profile)
                document.save()



        listing.shares = clean['shares']
        listing.price = clean['price']
        listing.save()
            
        return super(EditListing, self).form_valid(form)


class Requests(accounts_mixins.StaffOnly,
               statpages_mixins.TopMenu,
               generic.ListView):
    model = CompanyRequest
    context_object_name = 'company_requests'
    template_name = 'admindeck/requests.html'


class Thanks(accounts_mixins.StaffOnly,
             statpages_mixins.TopMenu,
             generic.TemplateView):

    template_name = 'admindeck/thanks.html'


class ApproveListing(accounts_mixins.StaffOnly,
                     generic.View):

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            result = {'success': False}
            listging_id = request.POST.get('id',None)
            if listging_id:
                try:
                    listing = models.Listing.objects.get(pk=listging_id)
                except:
                    raise Http404

                listing.is_approved = True
                print timezone.now
                listing.approvedon = timezone.now()
                listing.expireson = timezone.now() + datetime.timedelta(days=60)
                listing.save()
                result['success'] = True

                return HttpResponse(json.dumps(result), content_type='application/json')
        raise Http404


class RemoveImage(accounts_mixins.StaffOnly, generic.View):

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            result = {'success': False}
            photo_id = request.POST.get('id', None)
            if photo_id:
                try:
                    Photo.objects.get(pk=photo_id).delete()
                    result['success'] = True
                except:
                    pass

                return HttpResponse(json.dumps(result), content_type='application/json')
        raise Http404


class RemoveDoc(accounts_mixins.StaffOnly, generic.View):

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            result = {'success': False}
            doc_id = request.POST.get('id', None)
            if doc_id:
                try:
                    Document.objects.get(pk=doc_id).delete()
                    result['success'] = True
                except:
                    pass

                return HttpResponse(json.dumps(result), content_type='application/json')
        raise Http404


class ChangeImage(accounts_mixins.StaffOnly, generic.View):

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            result = {'success': False}
            photo_id = request.POST.get('id', None)
            if photo_id:
                try:
                    photo = Photo.objects.get(pk=photo_id)
                    Photo.objects.filter(company=photo.company).update(is_main=False)
                    photo.is_main = True
                    photo.save()
                    result['success'] = True
                except:
                    pass

                return HttpResponse(json.dumps(result), content_type='application/json')
        raise Http404


class DoRequestCompany(generic.View):

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            result = {'success': False}
            url = request.POST.get('company_link', None)
            if url is not None:
                c = CompanyRequest.objects.create(url=url)
                if c.id:
                    result['success'] = True

            return HttpResponse(json.dumps(result), content_type='application/json')

        raise Http404


class ProccessedRequest(accounts_mixins.StaffOnly,
                        generic.View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            result = {'success': False}
            id = request.POST.get('id', None)
            if id is not None:
                CompanyRequest.objects.filter(id=id).update(done=True)
                result['success'] = True
            return HttpResponse(json.dumps(result), content_type='application/json')

        raise Http404
