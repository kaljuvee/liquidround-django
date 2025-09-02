from django.conf import settings
from django import forms
from django.core.mail import mail_admins, send_mail

from django.template.loader import get_template, render_to_string
from django.template import Context

from django.contrib.auth import authenticate

from . import models

class MyUserForm(forms.Form):

    # the request is now available, add it to the instance data
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(MyUserForm, self).__init__(*args, **kwargs)


class LoginForm(MyUserForm):
    email = forms.EmailField(
            widget=forms.TextInput(
                    attrs={'placeholder': 'E-mail', 'class': 'form-control'}
                )
        )
    password = forms.CharField(
            max_length=100,
            widget=forms.PasswordInput(
                    attrs={'placeholder': 'Password', 'class': 'form-control'}
                )
        )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        user = authenticate(
                email=email,
                password=password
            )
        if user is None:
            raise forms.ValidationError(
                "Email or password incorrect"
            )
        else:
            if not user.is_active:
                raise forms.ValidationError(
                    "Account should be activated by email"
            )


class RegisterForm(MyUserForm):
    full_name = forms.CharField(
            max_length=120,
            widget=forms.TextInput(
                    attrs={'placeholder': 'Full Name', 'class': 'form-control'}
                )
        )
    phone = forms.CharField(
            max_length=20,
            widget=forms.TextInput(
                    attrs={'placeholder': 'Phone Number', 'class': 'form-control'}
                )
        )
    email = forms.EmailField(
            widget=forms.TextInput(
                    attrs={'placeholder': 'E-mail', 'class': 'form-control'}
                )
        )
    password = forms.CharField(
            max_length=100,
            widget=forms.PasswordInput(
                    attrs={'placeholder': 'Password', 'class': 'form-control'}
                )
        )
    password_confirm = forms.CharField(
            max_length=100,
            widget=forms.PasswordInput(
                    attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}
                )
        )
    CERTS = (
        ('hnwi', 'I certify that I am a High Net Worth Investor'),
        ('si', 'I certify that I am a qualified Sophisticated Investor'),
    )
    certified = forms.ChoiceField(
            choices= CERTS,
            widget=forms.RadioSelect()
        )

    agree = forms.BooleanField(label="I agree to the terms above and recognise that investing in private stocks carries a number of unique risks")

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        email = cleaned_data.get("email")
        agree = cleaned_data.get("agree")

        print(agree)
        if email:
            check = models.Profile.objects.filter(user__email__iexact=email)
            if check.count() > 0:
                raise forms.ValidationError(
                    "Email you provided is already registered"
                )

        if password != password_confirm:
            raise forms.ValidationError(
                "Password Confirmation doesn't match Password"
            )

        if not agree:
            raise forms.ValidationError(
                "You should agree with terms to proceed registration"
            )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.initial['certified'] = 'hnwi'

    def mail(self, code):
        url = settings.ALLOWED_HOSTS[0]
        cleaned_data = super(RegisterForm, self).clean()
        name = cleaned_data.get('full_name')
        email = cleaned_data.get('email')

        html_email = render_to_string('emails/activation.html', {
            'name': name,
            'link': 'http://%s/account/activate/%s/' % (url, code)
        })
        try:
            send_mail(
                '[LiquidRound] Registration Email',
                html_email,
                'noreply@liquidround.co.uk',
                [email],
                fail_silently = True,
                html_message = html_email
            )
        except:
            pass


class ProfileForm(forms.Form):
    phone = forms.CharField(
                max_length=30,
                widget=forms.TextInput(
                    attrs={'placeholder': 'Phone', 'class': 'form-control'}
                )
            )