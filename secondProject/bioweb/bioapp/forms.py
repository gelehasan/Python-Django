from django import forms

class ECForm(forms.Form):
    ec_name = forms.CharField(label="EC Name", max_length=100)
