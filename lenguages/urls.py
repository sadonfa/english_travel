from django.urls import path
from . import views

urlpatterns = [
    path('idiomas/', views.lenguages, name="lenguage"),
    path('idioma/<int:id>/', views.pglenguages, name="lengua")
]