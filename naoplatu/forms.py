#encoding:utf-8
from django import forms


class NaoplatuForm(forms.Form):

    org_type = forms.CharField()
    org_name = forms.CharField()
    org_phone_type = forms.CharField()
    org_phone_value = forms.CharField()
    org_address = forms.CharField()
    org_inn = forms.CharField()
    org_cat = forms.CharField()
    number = forms.CharField()
    date = forms.DateField()
    org_bank = forms.CharField()
    org_bic = forms.CharField()
    org_bank_number = forms.CharField()
    wtf_number = forms.CharField()
    client_type = forms.CharField()
    client_name = forms.CharField()


class NaoplatuFilesForm(forms.Form):

    logo = forms.FileField()
    director_sign = forms.FileField()
    booker_sign = forms.FileField()
    printing = forms.FileField()
