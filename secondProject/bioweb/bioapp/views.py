from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *  
from django.views.generic import UpdateView
# Create your views here.

def index(request):
    genes=Gene.objects.all()
    return render(request, 'bioapp/index.html', {'genes':genes})



def gene(request,pk):
    gene=Gene.objects.get(pk=pk)
    gene.access +=1
    print("Gene Record: " , pk, " Access count : ", str(gene.access))
    gene.save()
    return render(request,'bioapp/gene.html', {'gene':gene})

class GeneUpdate(UpdateView):
    model=Gene
    fields=['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon', 'sequencing', 'ec']
    template_name_suffix='_update_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['master_genes'] = Gene.objects.all()
        return context

    

def delete (request, pk):
    GeneAttributeLink.objects.filter(gene_id=pk).delete()
    Gene.objects.filter(pk=pk).delete()
    return HttpResponseRedirect("/")

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


def create_gene(request):
    if request.method == 'POST':
        form = GeneForm(request.POST)
        if form.is_valid():
            gene = form.save()
            return HttpResponseRedirect('/create_gene/')
        else:
            return render(request, 'genedata/create_gene.html', {'error': 'failed','master_genes': master_genes,'form': form})
    else:
        master_genes = Gene.objects.all()
        form = GeneForm()

    
    return render(request, 'bioapp/create_gene.html', {'form': form, 'master_genes': master_genes})
