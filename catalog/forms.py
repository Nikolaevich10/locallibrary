
from django import forms
from django.core.exceptions import ValidationError
from django import forms




class HelpForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)