from django import forms
from .models import EventsGift, GiftDescript


class EventsGiftForm(forms.ModelForm):

    class Meta:
        model = EventsGift
        fields = ('id_event', 'id_gift',)


class SendMSG(forms.Form):
    msg = forms.CharField(label='Message', max_length=500)
    contacts = forms.CharField(label='Contacts', required=False)
    img = forms.ImageField(required=False)


class GiftDescriptForm(forms.ModelForm):

    class Meta:
        model = GiftDescript
        fields = ('name', 'cnt', 'img')
