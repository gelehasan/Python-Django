from django.shortcuts import render

from .models import *
# Create your views here.
def index(request):
    responseString= Hello.objects.all()[0]
    return render(request, 'helloworld/index.html', {'data':responseString})