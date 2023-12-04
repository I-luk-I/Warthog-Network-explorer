from django import forms

class FindForm(forms.Form):
    wallet = forms.CharField(max_length=100)