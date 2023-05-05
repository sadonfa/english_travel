from django.shortcuts import render
from travel.models import Travels
from lenguages.models import Lenguages

# Create your views here.

def home(request):
    
    travels = Travels.objects.all().order_by('-create_ad')[:3]
    lengs = Lenguages.objects.all().order_by('id')[:3]

    return render(request, "home.html",{
        'travels': travels,
        'lengs': lengs
    })

