from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *  
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView

class GeneList(ListView):
    model= Gene
    context_object_name= "genes"
    template_name='bioapp/index.html'




class GeneDetail(DetailView):
    model=Gene
    context_object_name= "gene"
    template_name='bioapp/gene.html'
    
class GeneUpdate(UpdateView):
    model=Gene
    fields=['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon', 'sequencing', 'ec']
    template_name_suffix='_update_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

    


class GeneDelete(DeleteView):
    model=Gene
    success_url="/"


def create_ec(request):
    master_genes=Gene.objects.all()
    if request.method == 'POST':
        form = ECForm(request.POST)
        if form.is_valid():
            ec = Ec()
            ec.ec_name = form.cleaned_data['ec_name']
            ec.save()
            return HttpResponseRedirect('/create_ec/')
    else:
        ecs = Ec.objects.all()
        form = ECForm()
    return render(request, 'bioapp/ec.html', {'form': form, 'ecs': ecs, 'master_genes':  master_genes})


class GeneCreate(CreateView):
    model=Gene
    template_name='bioapp/create_gene.html'
    form_class= GeneForm
    success_url="/"
