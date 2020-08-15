from django.contrib import admin
from api.core.models import create_user, create_event

admin.site.register(create_user)
admin.site.register(create_event)