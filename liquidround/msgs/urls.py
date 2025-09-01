from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^request_contacts/$', views.RequestContacts.as_view(), name='request_contacts'),
]