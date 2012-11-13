# encoding:utf-8
from annoying.decorators import render_to
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin
from naoplatu.forms import InvoiceForm, PositionFormSet, InvoiceFilesForm, \
    SendMailForm, RegularForm
from naoplatu.models import Invoice
from webodt.converters import converter
from webodt.shortcuts import render_to_response
import copy
import webodt


@render_to('naoplatu/index.html')
def naoplatu(request):
    return {}


@render_to('naoplatu/invoice_list.html')
def invoice_list(request):
    invoices = Invoice.objects.filter(user=request.user).order_by('-created')
    return {'invoices': invoices}


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
    attach_name_template = 'invoice-{0}.pdf'
    one_send_conf = {
        'template_name': {
            'subject': 'mails/one_send_subject.txt',
            'text': 'mails/one_send_text_content.txt',
        },
        'success_message': u'Письмо с выставленным счётом успешно отправлено',
    }
    remind_send_conf = {
        'template_name': {
            'subject': 'mails/remind_send_subject.txt',
            'text': 'mails/remind_send_text_content.txt',
        },
        'success_message': u'Письмо с напоминанием об оплате счёта отправлено',
    }

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
            is_remind = kwargs.get('remind')
            conf = is_remind and self.remind_send_conf or self.one_send_conf
            subject = render_to_string(
                conf['template_name']['subject'], doc_context,
            ).strip()
            text_content = render_to_string(
                conf['template_name']['text'], doc_context,
            ).srtip()
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            filename = self.attach_name_template.format(invoice.id)
            msg.attach(filename, pdf.read(), 'application/pdf')
            msg.send()
            messages.success(request, conf['success_message'])
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

    @require_POST
    def dublicate(self, request, *args, **kwargs):
        # TODO: Проверить
        new_invoice = copy.deepcopy(self.invoice)
        new_invoice.number += 1
        new_invoice.save()
        messages.success(request, u'Счёт успешно продублирован')
        return redirect(new_invoice.get_absolute_url())


    def edit(self, request, *args, **kwargs):
        # TODO: Сделать
        pass

    def mark_paid(self, request, *args, **kwargs):
        # TODO: Проверить
        self.invoice.status = Invoice.STATUS_PAID
        self.invoice.save()
        messages.success(request, u'Счёт помечен как оплаченный')
        return redirect(self.invoice.get_absolute_url())

    def close_with_act(self, request, *args, **kwargs):
        # TODO: Сделать форму
        pass

    def delete(self, request, *args, **kwargs):
        self.invoice.is_deleted = True
        self.invoice.save()
        messages.success(request, u'Счёт успешно удалён')
        redirect_to_url = reverse('naoplatu-invoice-list')
        return redirect(redirect_to_url)


class ActDetailView(View, TemplateResponseMixin):

    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        # TODO: Сделать
        context = {}
        return self.render_to_response(context)

    def edit_description(self, *args, **kwargs):
        # TODO: Сделать
        pass

    def send_email(self, request, *args, **kwargs):
        # TODO: Сделать
        pass

    def download(self, request, *args, **kwargs):
        # TODO: Сделать
        pass

    def delete(self, request, *args, **kwargs):
        self.act.is_deleted = True
        self.act.save()
        messages.success(request, u'Акт успешно удалён')
        return redirect(self.invoice.get_absolute_url())
