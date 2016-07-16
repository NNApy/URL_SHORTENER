from django import forms

class UrlForm(forms.Form):
    long_url = forms.URLField()