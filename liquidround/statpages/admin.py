from django.contrib import admin

# Register your models here.
from statpages.models import Page, Slider

admin.site.register(Page)
admin.site.register(Slider)