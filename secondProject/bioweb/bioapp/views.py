from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
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