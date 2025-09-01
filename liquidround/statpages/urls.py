from django.conf.urls import include, url
from statpages import views

urlpatterns = [
    url(r'^(?P<slug>[-\w_\d]{1,100})/$', views.Show.as_view(), name='page'),
    url(r'^$', views.Home.as_view(), name='home'),
]