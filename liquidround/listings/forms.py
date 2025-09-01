from django import forms
from accounts.forms import MyUserForm

class ListingForm(MyUserForm):
    company = forms.CharField(max_length=128)
    industry = forms.CharField(max_length=128)
    website = forms.URLField()
    specificrole = forms.CharField(max_length=256)
    shares = forms.IntegerField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    listing_type = forms.CharField(max_length=15)
    company_id = forms.IntegerField(required=False)

class EditListing(forms.Form):
    published = forms.BooleanField(required=False)
    company = forms.CharField(max_length=128)
    industry = forms.CharField(max_length=128)
    website = forms.URLField()
    specificrole = forms.CharField(max_length=256)
    shares = forms.IntegerField()
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    listing_type = forms.CharField(max_length=15)
    company_id = forms.IntegerField(required=False)

    country = forms.CharField(max_length=30)
    city = forms.CharField(max_length=30)
    summary = forms.CharField(max_length=4000,
            widget=forms.Textarea()
        )
    pre_emption_rights = forms.BooleanField(required=False)
    voting_rights = forms.BooleanField(required=False)
    class_a = forms.BooleanField(required=False)
    class_b = forms.BooleanField(required=False)
    funding_stage = forms.CharField(max_length=30)