from django.contrib import admin

# Register your models here.
from . import models

class ListingAdmin(admin.ModelAdmin):
    fields = ['company', 'user', 'shares', 'price', 'listing_type', 'createdon', 'is_approved', 'approvedon', 'is_closed', 'is_deleted', 'expireson']

    readonly_fields = ('approvedon', 'createdon')
    list_display = ('company', 'user', 'shares','price', 'listing_type', 'createdon', 'is_approved', 'approvedon', 'is_closed', 'is_deleted')
    list_filter = ['listing_type', 'is_approved', 'is_deleted']


admin.site.register(models.Listing, ListingAdmin)