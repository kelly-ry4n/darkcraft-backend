
from django import forms

class RequestWorldSaveForm(forms.Form):

    signature = forms.CharField(max_length=255)