from django import forms


class Notify(forms.Form):
    receptor  = forms.IntegerField(label="گیرنده")
    message = forms.CharField(widget=forms.Textarea,label="متن پیام")


class gas_co2_alert(forms.Form):
    co = forms.IntegerField()