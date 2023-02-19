from django import forms


class JobForm(forms.Form):
    keywords = forms.CharField(label="keywords")
    location = forms.CharField(label="location")


class ButtonForm(forms.Form):
    favorite = forms.BooleanField(required=False)
