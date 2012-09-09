#encoding:utf-8
from annoying.decorators import render_to
from naoplatu.forms import NaoplatuForm


@render_to('naoplatu/index.html')
def naoplatu(request):
    return {}


@render_to('naoplatu/invoice.html')
def invoice(request):
    form = NaoplatuForm(request.GET or None)
    return {'form': form}
