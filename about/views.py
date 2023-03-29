from django.shortcuts import render
from about.models import About

# Create your views here.
def about(request):

    about = About.objects.all()

    return render(request, 'about.html', {
        'titulo': 'Nosotros',
        'cont_about': about
    })