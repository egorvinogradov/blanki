#coding:utf8
from django.conf.urls.defaults import url, patterns
from naoplatu.views import CreateInvoiceView, InvoiceDetailView

urlpatterns = patterns('naoplatu.views',
    url(r'^$', 'naoplatu', name='blanki-naoplatu'),
    url(r'^invoice/list/$', 'invoice_list', name='naoplatu-invoice-list'),
    url(r'^invoice/$', CreateInvoiceView.as_view(), name='naoplatu-create-invoice'),
    url(r'^invoice/(?P<invoice_id>\d+)/$',
        InvoiceDetailView.as_view(), name='naoplatu-invoice-detail'),
)
