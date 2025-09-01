import json
from django.http import Http404, HttpResponse
from django.shortcuts import render

from django.core.mail import mail_admins, send_mail
from django.template import Context

from django.template.loader import get_template

from django.views import generic

# Create your views here.
from . import models
from listings.models import Listing


class RequestContacts(generic.View):
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            result = {'success': False}
            if request.user.is_authenticated():

                listing_id = request.POST.get('id', None)
                if listing_id:
                    try:
                        listing = Listing.objects.get(pk=listing_id)
                    except:
                        return HttpResponse(json.dumps(result), content_type='application/json')

                    if listing.listing_type == 'equity':
                        subject = 'Interest in your equity'
                        html_email = get_template('emails/equity.html').render(Context({
                                'user_name': listing.user.user.first_name,
                                'requester_name': "%s %s" % (request.user.first_name, request.user.last_name),
                                'requester_email': request.user.email,
                            }))
                    else:
                        subject = '%s %s is looking to sell %s' % (request.user.first_name, request.user.last_name, listing.company.title)

                        html_email = get_template('emails/offer.html').render(Context({
                                'user_name': listing.user.user.first_name,
                                'requester_name': "%s %s" % (request.user.first_name, request.user.last_name),
                                'requester_email': request.user.email,
                            }))

                    email = listing.user.user.email
                
                    try:
                        send_mail(
                            subject,
                            html_email,
                            'noreply@liquidround.co.uk',
                            [email],
                            fail_silently = True,
                            html_message = html_email
                        )
                    except:
                        pass

                    models.Message.objects.create(
                                   user_from=request.user.profile,
                                   user_to=listing.user,
                                   subject=subject,
                                   new=True,
                                   text=html_email,
                                   listing=listing
                            )
                    result['success'] = True




            return HttpResponse(json.dumps(result), content_type='application/json')
        raise Http404