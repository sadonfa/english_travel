from django.shortcuts import render

# Create your views here.

def lenguages(request):
    return render(request, 'lenguages.html',{
        'title':'Idiomas'
    })

def pglenguages(request):
    return render(request, 'pg-lenguage.html',{
        'title':'titulo principal'
    })