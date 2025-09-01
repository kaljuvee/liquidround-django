from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.Deck.as_view(), name='deck'),
    url(r'^sellers/$', views.Listings.as_view(listing_type='equity'), name='sellers'),
    url(r'^buyers/$', views.Listings.as_view(listing_type='offer'), name='buyers'),
    url(r'^edit/(?P<listing_id>(\d+))/$', views.EditListing.as_view(), name='edit'),
    url(r'^thanks/$', views.Thanks.as_view(), name='thanks'),
    url(r'^approve/$', views.ApproveListing.as_view(), name='approve'),
    url(r'^remove_image/$', views.RemoveImage.as_view(), name='remove_image'),
    url(r'^remove_doc/$', views.RemoveDoc.as_view(), name='remove_doc'),
    url(r'^change_main_image/$', views.ChangeImage.as_view(), name='change_image'),
    url(r'^users/$', views.Users.as_view(), name='users'),
    url(r'^documents/$', views.Documents.as_view(), name='documents'),
    url(r'^statistic/$', views.Statistic.as_view(), name='statistic'),
    url(r'^requests/$', views.Requests.as_view(), name='requests'),
    url(r'^proccessed/$', views.ProccessedRequest.as_view(), name='proccessed'),
]