from django.urls import path
from . import views

urlpatterns = [
    path("", views.produit_list, name='produit_list'),
]