from django import forms

class ParserForm(forms.Form):
    url = forms.URLField(blank=None)
