from django.urls import path
from . import views

urlpatterns = [
    path('idiomas/', views.lenguages, name="lenguage"),
    path('idioma/', views.pglenguages, name="lengua")
]