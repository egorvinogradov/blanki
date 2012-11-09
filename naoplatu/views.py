# encoding:utf-8
from annoying.decorators import render_to
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import render_to_string
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin
from naoplatu.forms import InvoiceForm, PositionFormSet, InvoiceFilesForm, \
    SendMailForm, RegularForm
from webodt.converters import converter
from webodt.shortcuts import render_to_response
import webodt


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
    document_name = 'naoplatu/docs/invoice.odt'
    one_send_subject_template_name = 'mails/one_send_subject.txt'
    one_send_text_template_name = 'mails/one_send_text_content.txt'
    one_send_html_template_name = 'mails/one_send_html_content.html'
    one_filename_template = 'invoice-{0}.pdf'
    one_send_success_message = u'Письмо с выставленным счётом успешно отправлено'

    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        # TODO: Сделать
        context = {}
        return self.render_to_response(context)

    def download(self, request, *args, **kwargs):
        # TODO: Сделать
        invoice_format = kwargs['format']
        filename = 'test_filename'
        return render_to_response(self.document_name, {
            'invoice': self.invoice,
        }, filename=filename, format=invoice_format)

    def send_email(self, request, *args, **kwargs):
        # TODO: Проверить, а также сделать from_email
        form = SendMailForm(request.POST or None, instance=self.invoice)
        if form.is_valid():
            invoice = form.save()
            to = form.cleaned_data['org_email']
            template = webodt.ODFTemplate(self.document_name)
            doc_context = {'invoice': invoice}
            document = template.render(Context(doc_context))
            pdf = converter().convert(document, format='pdf')
            subject = render_to_string(
                self.one_send_subject_template_name, doc_context,
            ).strip()
            text_content = render_to_string(
                self.one_send_text_template_name, doc_context,
            ).srtip()
            html_content = render_to_string(
                self.one_send_html_template_name, doc_context,
            ).srtip()
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            filename = self.one_filename_template.format(invoice.id)
            msg.attach(filename, pdf.read(), 'application/pdf')
            msg.send()
            messages.success(request, self.one_send_success_message)
        context = {'mail_form': form, 'invoice': invoice}
        return self.render_to_response(context)

    def regular(self, request, *args, **kwargs):
        # TODO: Проверить
        form = RegularForm(request.POST or None, instance=self.invoice)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.is_regular = True
            invoice.save()
        context = {'regular_form': form, 'invoice': invoice}
        return self.render_to_response(context)
