from django.urls import re_path as url

from . import views
urlpatterns = [
    url(r'^create/(?P<listing_type>(equity|offer))/$', views.CreateListing.as_view(), name='create'),
    url(r'^success/(?P<listing_type>(equity|offer))/$', views.Created.as_view(), name='success'),
    url(r'^delete/$', views.MarkAs.as_view(mark='deleted'), name='delete'),
    url(r'^sold/$', views.MarkAs.as_view(mark='closed'), name='closed'),
    url(r'^prolong/(?P<code>[-_\w\d]+)/$', views.Prolong.as_view(), name='prolong'),
]