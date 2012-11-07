# coding:utf-8
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationForm as DefaultRegistrationForm


class RegistrationForm(DefaultRegistrationForm):

    username = forms.CharField(widget=forms.HiddenInput, required=False)
    password2 = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        cleaned_data = cleaned_data.copy()
        cleaned_data['username'] = cleaned_data.get('email')
        cleaned_data['password2'] = cleaned_data.get('password1')
        return cleaned_data

    def clean_username(self):
        return self.cleaned_data['username']

    def clean_email(self):
        """
        Validate that the username is alphanumeric and is not already
        in use.
        
        """
        existing = User.objects.filter(email__iexact=self.cleaned_data['email'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that email already exists."))
        else:
            return self.cleaned_data['email'].lower()
