from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.travel, name="travels"),
    path('tour/<int:id>/', views.tour, name="tour")
]