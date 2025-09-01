# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import datetime

from django.db.models import IntegerField, Sum, Case, When, Q
from django.shortcuts import render
from django.http import HttpResponse, Http404


from django.views import generic
from . import models
from statpages import mixins
# Create your views here.

class Company(mixins.TopMenu, generic.DetailView):
    model = models.Company
    context_object_name = 'company'
    template_name = 'companies/company.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            nots = request.user.profile.notifications.filter(company__slug=self.kwargs['slug'])
            if nots.count() > 0:
                nots.delete()
        return super(Company, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super(Company, self).get_queryset()
        qs = qs.filter(published=True)
        return qs


    def get_context_data(self, *args, **kwargs):
        context = super(Company, self).get_context_data(*args, **kwargs)
        context['active_app'] = 'company'
        if self.object:
            context['equities'] = self.object.listings \
                   .filter(listing_type='equity', 
                           is_approved=True, 
                           is_closed=False,
                           is_deleted=False,
                           expireson__gt=datetime.datetime.now())
            context['offers'] = self.object.listings \
                   .filter(listing_type='offer',
                           is_approved=True,
                           is_closed=False,
                           is_deleted=False,
                           expireson__gt=datetime.datetime.now())
            context['history'] = self.object.listings \
                    .filter(
                        is_approved=True,
                        is_closed=True,
                        is_deleted=False
                    )
        if self.request.user.is_authenticated():
            context['requested'] = self.request.user.profile.msgs_from \
                .filter(listing__isnull=False).values_list('listing_id', flat=True)
            print context['requested']
        return context

class Companies(mixins.TopMenu, generic.ListView):

    model = models.Company
    template_name = 'companies/all.html'
    context_object_name = 'companies'
    paginate_by = 10
    filters = {}

    def dispatch(self, request, *args, **kwargs):
        if self.request.is_ajax():
            self.template_name = 'companies/all_unstyled.html'

        self.filters['activities'] = request.GET.getlist('activity[]')
        self.filters['funding'] = request.GET.getlist('funding[]')
        self.filters['industry'] = request.GET.getlist('industry[]')
        self.filters['title'] = request.GET.get('title', None)
        print self.filters
        return super(Companies, self).dispatch(request, *args, **kwargs)

    def industries(self):
        return models.Industry.objects.all()

    def get_queryset(self):
        qs = super(Companies, self).get_queryset()
        qs = qs.annotate(
                equities=Sum(
                    Case(
                        When(listings__listing_type='equity',
                             listings__is_approved=True, 
                             listings__is_closed=False,
                             listings__expireson__gt=datetime.datetime.now(), 
                             then=1),
                        output_field=IntegerField()
                    ),
                ),
                offers=Sum(
                    Case(
                        When(listings__listing_type='offer', 
                             listings__is_approved=True, 
                             listings__is_closed=False,
                             listings__expireson__gt=datetime.datetime.now(), 
                             then=1),
                        output_field=IntegerField()
                    ),
                )
            ).order_by('equities','offers') \
            .filter(published=True)


        activity = True if len(self.filters['activities']) > 0 else False
        funding = True if len(self.filters['funding']) > 0 else False
        industry = True if len(self.filters['industry']) > 0 else False
        title = True if self.filters['title'] is not None else False


        if activity:
            if 'offer' in self.filters['activities'] and 'equity' in self.filters['activities']:
                qs = qs.filter(Q(offers__gt=0)|Q(equities__gt=0))
            elif 'offer' in self.filters['activities'] and 'equity' not in self.filters['activities']:
                qs = qs.filter(offers__gt=0)
            elif 'offer' not in self.filters['activities'] and 'equity' in self.filters['activities']:
                qs = qs.filter(equities__gt=0)
            else:
                pass

        if funding:
            qs = qs.filter(funding_stage__in=self.filters['funding'])

        if industry:
            qs = qs.filter(industry_id__in=self.filters['industry'])

        if title:
            qs = qs.filter(title__icontains=self.filters['title'])

        return qs

    def get_context_data(self, *args, **kwargs):
        context = super(Companies, self).get_context_data(*args, **kwargs)
        context['active_app'] = 'company'
        return context


class SearchCompanies(generic.View):
    def get(self, request):
        if request.is_ajax():
            result = {'success': False}
            q = request.GET.get('query', None)
            if q:
                companies = models.Company.objects.filter(title__icontains=q)
                print companies.count()
                result = {'query': q}
                result['suggestions'] = [c.option_dict() for c in companies]


            return HttpResponse(json.dumps(result), content_type='application/json')
        raise Http404


class GetCompany(generic.View):
    def post(self, request):
        if request.is_ajax():
            result = {'success': False}
            cid = request.POST.get('id', None)
            if cid is not None:
                try:
                    company = models.Company.objects.get(pk=cid)
                    result['company'] = company.safe_dict()
                    result['success'] = True
                except:
                    pass
            return HttpResponse(json.dumps(result), content_type='application/json')
        raise Http404

class Watch(generic.View):

    def post(self, request):
        if request.is_ajax():
            result = {'success': False}
            cid = request.POST.get('id', None)
            if request.user.is_authenticated():
                if cid is not None:
                    company = models.Company.objects.get(pk=cid)
                    result['status'] = request.user.profile.watch(cid)
                    if result['status']:
                        result['success'] = True
            return HttpResponse(json.dumps(result), content_type='application/json')
        raise Http404