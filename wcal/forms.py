from django import forms

from .models import Event

class EventForm(forms.ModelForm):
# из чего состоит событие
# это чтобы заполнять
    class Meta:
        model = Event
        fields = ('title', 'text', 'event_date',)
