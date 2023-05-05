from django.shortcuts import render
from .models import Lenguages

# Create your views here.

def lenguages(request):
    lengs = Lenguages.objects.order_by("id")

    return render(request, 'lenguages.html',{
        'lengs': lengs,
        'title':'Cursos de Ingles'
    })

def pglenguages(request, id):

    leng = Lenguages.objects.get(id=id)

    return render(request, 'pg-lenguage.html',{
        'title':'titulo principal',
        'leng': leng
    })