from django import forms
from .models import EventsGift


class EventsGiftForm(forms.ModelForm):

    class Meta:
        model = EventsGift
        fields = ('id_event', 'id_gift',)
