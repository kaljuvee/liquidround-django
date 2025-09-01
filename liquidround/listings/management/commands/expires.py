import datetime
import hashlib
from django.core.management.base import BaseCommand, CommandError

from django.core.mail import mail_admins, send_mail
from django.template import Context

from django.template.loader import get_template

from listings import models

class Command(BaseCommand):

    help = 'Checks for expired listings and sends email to user with link to increase expire date for 2 months (60 days)'

    def handle(self, *args, **options):
        expired = models.Listing.objects.filter(expireson__lte=datetime.datetime.now(), prolong_messaged=False)

        self.stdout.write('Found %s expired listings' % expired.count())
        for e in expired:
            code = hashlib.md5(str(e.user.user.username) + str(e) + str(datetime.datetime.now())).hexdigest()
            subject = 'Your LiquidRound listing has expired'

            html_email = get_template('emails/expired.html').render(Context({
                    'user_name': e.user.user.first_name,
                    'code': code,
                }))

            email = e.user.user.email
        
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
            e.prolong_code = code
            e.prolong_messaged = True
            e.save()

            self.stdout.write('Listing %s by user %s %s send mail | %s' % (e.id, e.user.user.first_name, e.user.user.last_name, code))
        # for poll_id in options['poll_id']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write('Successfully closed poll "%s"' % poll_id)