from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.CompanyRequest)
class RequestListingAdmin(admin.ModelAdmin):
    list_display = 'id', 'url', 'createdon', 'updatedon', 'done'