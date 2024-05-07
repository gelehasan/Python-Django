from django.shortcuts import render

from .models import *
# Create your views here.
def index(request):
    responseString= Hello.objects.all()[0]
    return render(request, 'helloworld/index.html', {'data':responseString})


def simple_view(request):
    addresses=Address.object.all()
    first_address=addresses[0]
    resident_name=str(first_address.resident)
    return render(request, 'helloworld/simple.html', {"address":first_address, "name":resident_name})