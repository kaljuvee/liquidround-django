from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from . import models
# Register your models here.
class ProfileInline(admin.StackedInline):
    model = models.Profile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(UserAdmin):
    view_on_view = True
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(models.Notification)
admin.site.register(User, UserAdmin)