from django.urls import re_path
from statpages import views

app_name = 'statpages'

urlpatterns = [
    re_path(r'^(?P<slug>[-\w_\d]{1,100})/$', views.Show.as_view(), name='page'),
    re_path(r'^$', views.Home.as_view(), name='home'),
]