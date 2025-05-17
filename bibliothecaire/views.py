from django.shortcuts import render, redirect
from .models import Livre, Cd, Dvd, Jeux_de_plateau
from .forms import LivreForm

# Create your views here.


def accueil_bibliothecaire(request):
    form = LivreForm()

    if request.method == 'POST':
        form = LivreForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
        
    else:
        form = LivreForm()


    context = {"livre" : Livre.objects.all(),
               "dvd" : Dvd.objects.all(),
               "cd" : Cd.objects.all(),
               "jeux_de_plateau" : Jeux_de_plateau.objects.all(),
               "form": form}
    
    return render(request, 'accueil_bibliothecaire.html', context)


