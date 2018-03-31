from django import forms

class ParserForm(forms.Form):
    url = forms.URLField(required=True)
