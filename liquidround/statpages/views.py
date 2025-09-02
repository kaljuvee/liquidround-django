import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import IntegerField, Sum, Case, When, Q

from django.views.generic import TemplateView
from django.views.generic import DetailView
from django.views.generic import ListView

from statpages.models import Page, Slider
from statpages.mixins import TopMenu

from companies.models import Company


class Home(TopMenu, TemplateView):
    template_name = "simple_home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['active_app'] = 'home'
        context['companies'] = Company.objects.all() \
            .annotate(
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
            ).filter(Q(equities__gt=0)|Q(offers__gt=0)) \
            .filter(published=True) \
            .order_by('equities','offers')[:4]
        
        context['slider'] = Slider.objects.all().order_by('position')
        return context


class Show(TopMenu, DetailView):
    model = Page
    template_name = 'statpages/page.html'

    def get_context_data(self, *args, **kwargs):
        context = super(Show, self).get_context_data(*args, **kwargs)
        context['active_app'] = 'about'
        if self.object.slug == 'how-it-works':
            context['active_app'] = 'howitworks'
        return context
