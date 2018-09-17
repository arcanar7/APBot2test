from django import forms
from .models import EventsGift


class EventsGiftForm(forms.ModelForm):

    class Meta:
        model = EventsGift
        fields = ('id_event', 'id_gift',)


class SendMSG(forms.Form):
    msg = forms.CharField(label='Message', max_length=500)
    contacts = forms.CharField(label='Contacts', required=False)
