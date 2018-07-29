from django import forms
from .models import EventsDescript


class EventForm(forms.ModelForm):

    class Meta:
        model = EventsDescript
        fields = ('name', 'descript',)
