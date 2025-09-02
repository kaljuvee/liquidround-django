from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^register/$', views.Register.as_view(), name='register'),
    url(r'^thanks/$', views.RegisterThanks.as_view(), name='thanks'),
    url(r'^activate/(?P<code>[\w\d]+)/$', views.RegisterActivation.as_view(), name='activate'),
    url(r'^login/$', views.Signin.as_view(), name='login'),
    url(r'^logout/$', views.signoff, name='logout'),
    url(r'^profile/$', views.Profile.as_view(), name='profile'),
    url(r'^profile/edit/$', views.EditProfile.as_view(), name='edit_profile'),
]