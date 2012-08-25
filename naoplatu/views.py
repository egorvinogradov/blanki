#encoding:utf-8
from annoying.decorators import render_to


#@render_to('naoplatu/index.html')
@render_to('naoplatu/invoice.html')
def naoplatu(request):
    return {}
