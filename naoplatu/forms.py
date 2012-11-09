# encoding:utf-8
from django import forms
from django.forms.formsets import formset_factory
from naoplatu.models import Invoice, InvoicePosition


class InvoiceForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = [
            'org_type', 'org_name', 'org_phone_type', 'org_phone_value',
            'org_address', 'org_inn', 'org_cat', 'number', 'date', 'org_bank',
            'org_bic', 'org_bank_number', 'wtf_number', 'client_type',
            'client_name',
        ]


class InvoiceFilesForm(forms.ModelForm):

    class Meta:
        model = Invoice
        fields = ['logo', 'director_sign', 'booker_sign', 'printing']


class PositionForm(forms.Form):

    class Meta:
        model = InvoicePosition
        fields = ['name', 'pos_type', 'number', 'price']

PositionFormSet = formset_factory(PositionForm)


class SendMailForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(SendMailForm, self).__init__(*args, **kwargs)
        self.fields['org_email'].required = True

    class Meta:
        model = Invoice
        fields = ['org_email']


class RegularForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(RegularForm, self).__init__(*args, **kwargs)
        self.fields['org_email'].required = True
        self.fields['regular_period'].required = True

    class Meta:
        model = Invoice
        fields = ['org_email', 'regular_period']
