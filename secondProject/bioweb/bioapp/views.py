from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    genes=Gene.objects.all()
    return render(request, 'bioapp/index.html', {'genes':genes})