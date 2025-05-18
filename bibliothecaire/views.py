from django.shortcuts import render, redirect, get_object_or_404
from .models import Livre, Cd, Dvd, Jeux_de_plateau
from .forms import LivreForm

# Create your views here.


def accueil_bibliothecaire(request):

    context = {"livre" : Livre.objects.all(),
               "dvd" : Dvd.objects.all(),
               "cd" : Cd.objects.all(),
               "jeux_de_plateau" : Jeux_de_plateau.objects.all(),
               }
    
    return render(request, 'accueil_bibliothecaire.html', context)

#Partie Livre-----------------------------------------------------------
def ajout_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
        
    else:
        form = LivreForm()
    
    return render(request, 'ajout_livre.html', {'form':form})


def modifier_livre(request, livre_id):
    livre = get_object_or_404(Livre, id = livre_id)

    if request.method == 'POST':
        form = LivreForm(request.POST, instance = livre)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
        
    else:
        form = LivreForm(instance = livre)
    
    return render(request, 'modifier_livre.html', {'form':form})


def supprimer_livre(request, livre_id):
    livre = get_object_or_404(Livre, id = livre_id)

    if request.method == 'POST':
        livre.delete()
        return redirect("bibliothecaire:accueil_bibliothecaire")
    
    return render(request, 'supprimer_livre.html', {'livre':Livre})


