from django import forms
from .models import EventsDescript


class EventForm(forms.ModelForm):

    class Meta:
        model = EventsDescript
        exclude = [""]
