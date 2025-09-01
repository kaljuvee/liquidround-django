from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.NewsList.as_view(), name='list'),
    url('^(?P<slug>[-\w_\d]{1,100})/$', views.NewsDetail.as_view(), name='detail'),
]