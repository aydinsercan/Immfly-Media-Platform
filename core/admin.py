from django.contrib import admin

# Register your models here.
from core.models import Channel, Content

admin.site.register(Channel)
admin.site.register(Content)
