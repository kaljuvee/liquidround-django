from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Temporarily comment out problematic URLs
    # path('admindeck/', include('admindeck.urls', namespace='admindeck')),
    # path('account/', include('accounts.urls', namespace='accounts')),
    # path('listing/', include('listings.urls', namespace='listing')),
    # path('company/', include('companies.urls', namespace='companies')),
    # path('messages/', include('msgs.urls', namespace='messages')),
    # path('news/', include('news.urls', namespace='news')),
    path('', include('statpages.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

