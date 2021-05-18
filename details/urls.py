from django.urls import path
from . import views

urlpatterns = [
    path('actor/', views.actor, name='actor'),
    path('film/', views.film, name='film'),
]
