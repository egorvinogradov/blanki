#encoding:utf-8
from annoying.decorators import render_to
from naoplatu.forms import NaoplatuForm, PositionFormSet, NaoplatuFilesForm


@render_to('naoplatu/index.html')
def naoplatu(request):
    return {}


@render_to('naoplatu/invoice.html')
def invoice(request):
    form = NaoplatuForm(request.GET or None)
    position_formset = PositionFormSet(request.GET or None)
    files_form = NaoplatuFilesForm(files=request.FILES or None)
    return {
        'form': form, 'position_formset': position_formset,
        'files_form': files_form,
    }
