# encoding:utf-8
from annoying.decorators import render_to
from django.shortcuts import redirect
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin
from naoplatu.forms import InvoiceForm, PositionFormSet, InvoiceFilesForm
from webodt.shortcuts import render_to_response


@render_to('naoplatu/index.html')
def naoplatu(request):
    return {}


class CreateInvoiceView(View, TemplateResponseMixin):

    template_name = 'naoplatu/create_invoice.html'

    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        form = InvoiceForm()
        position_formset = PositionFormSet()
        files_form = InvoiceFilesForm()
        context = {
            'form': form, 'position_formset': position_formset,
            'files_form': files_form,
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = InvoiceForm(request.POST)
        position_formset = PositionFormSet(request.POST)
        files_form = InvoiceFilesForm(request.POST, files=request.FILES)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.user = request.user
            invoice.save()
        if form.is_valid() and position_formset.is_valid():
            for position_form in position_formset:
                position = position_form.save(commit=False)
                position.invoice = invoice
                position.save()
        if form.is_valid() and files_form.is_valid():
            for key, val in files_form.cleaned_data.iteritems():
                setattr(invoice, key, val)
            invoice.save()
        if form.is_valid():
            return redirect(invoice.get_absolute_url())
        context = {
            'form': form, 'position_formset': position_formset,
            'files_form': files_form,
        }
        return self.render_to_response(context)


class InvoiceDetailView(View, TemplateResponseMixin):

    template_name = 'naoplatu/invoice_detail.html'

    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        # TODO: Сделать
        context = {}
        return self.render_to_response(context)

    def download(self, request, *args, **kwargs):
        # TODO: Сделать
        invoice_format = kwargs['format']
        template_name = 'naoplatu/docs/invoice.odt'
        filename = 'test_filename'
        return render_to_response(template_name, {
            'invoice': self.invoice,
        }, filename=filename, format=invoice_format)

    def send_email(self, request, *args, **kwargs):
        # TODO: Сделать
        pass
