from django import forms
from django.forms import ModelForm

from smart_road.models import Event

#
# class EventForm(forms.Form):
#     cell_name  = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":60}),label="شناسه cell")


class EventForm(ModelForm):

     class Meta:
         model = Event
         fields = ['cell_name']
         labels = {
             "cell_name": "شناسه سلول",
         }