from django.contrib import admin
from . import models


class Groupmemberinline(admin.TabularInline):
    model = models.Groupmember

admin.site.register(models.Group)
admin.site.register(models.Groupmember)

# Register your models here.
