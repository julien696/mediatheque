from django.urls import path
from . import views


app_name = 'bibliothecaire'

urlpatterns = [
    path('accueil', views.accueil_bibliothecaire, name = 'accueil_bibliothecaire'),
]