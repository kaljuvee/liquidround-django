from django.contrib import admin

# Register your models here.
from . import models

class TeamInline(admin.StackedInline):
    model = models.Teammate
    extra = 1

class DocumentsInline(admin.StackedInline):
    model = models.Document
    extra = 1

class PhotoInline(admin.StackedInline):
    model = models.Photo
    extra = 1

class CompanyAdmin(admin.ModelAdmin):
    save_as = True
    fields = ['title','slug','published','website','industry','role','country','city','summary','team_desc','pre_emption_rights','voting_rights','class_a','class_b','funding_stage']

    list_display = ('id','title','industry','role','pre_emption_rights','voting_rights','class_a','class_b','funding_stage','published')

    inlines = (TeamInline, DocumentsInline, PhotoInline)

admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.Industry)