from django.shortcuts import render
from bibliothecaire.models import Livre, Dvd, Cd, Jeux_de_plateau 

# Create your views here.


def accueil_membre(request):
    context = {"livre" : Livre.objects.all(),
               "dvd" : Dvd.objects.all(),
               "cd" : Cd.objects.all(),
               "jeux_de_plateau" : Jeux_de_plateau.objects.all()}
    return render(request, 'accueil_membre.html', context) 
