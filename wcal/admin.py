from django.contrib import admin
from .models import Event, EventDate

admin.site.register(Event)
# dg - Post - Events
# python manage.py createsuperuser
admin.site.register(EventDate)
