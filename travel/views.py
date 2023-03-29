from django.shortcuts import render
from .models import Travels

# Create your views here.

def travel(request):

    travels = Travels.objects.all()
   
    return render(request, 'travels.html', {
        'titulo': 'Paquetes Turisticos',
        'travels': travels
    })