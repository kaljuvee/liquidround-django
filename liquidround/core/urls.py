from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^admindeck/', include('admindeck.urls', namespace='admindeck')),
    url(r'^account/', include('accounts.urls', namespace='accounts')),
    url(r'^listing/', include('listings.urls', namespace='listing')),
    url(r'^company/', include('companies.urls', namespace='companies')),
    url(r'^messages/', include('msgs.urls', namespace='messages')),
    url(r'^news/', include('news.urls', namespace='news')),
    url(r'^', include('statpages.urls', namespace='statpages')),
]

if settings.DEBUG:
    urlpatterns += [
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
           {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
           {'document_root': settings.STATIC_ROOT}),
    ]