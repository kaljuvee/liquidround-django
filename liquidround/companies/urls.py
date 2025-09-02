from django.urls import re_path as url

from . import views
from admindeck.views import DoRequestCompany
urlpatterns = [
    url(r'^all/$', views.Companies.as_view(), name='all'),
    url(r'^watch/$', views.Watch.as_view(), name='watch'),
    url(r'^search/$', views.SearchCompanies.as_view(), name='search'),
    url(r'^get/$', views.GetCompany.as_view(), name='get_company'),
    url(r'^request/$', DoRequestCompany.as_view(), name='request_company'),
    url(r'^(?P<slug>[-\w\d_]+)/$', views.Company.as_view(), name='company'),
]