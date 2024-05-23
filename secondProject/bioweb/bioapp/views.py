from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *  
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


def delete (request, pk):
    GeneAttributeLink.objects.filter(gene_id=pk).delete()
    Gene.objects.filter(pk=pk).delete()
    return HttpResponseRedirect("/")

def create_ec(request):
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
    return render(request, 'bioapp/ec.html', {'form': form, 'ecs': ecs})