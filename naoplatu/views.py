#encoding:utf-8
from annoying.decorators import render_to


@render_to('naoplatu/index.html')
def naoplatu(request):
    return {}


@render_to('naoplatu/invoice.html')
def invoice(request):
    return {}
