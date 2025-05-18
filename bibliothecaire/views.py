from django.shortcuts import render, redirect, get_object_or_404
from .models import Livre, Cd, Dvd, Jeux_de_plateau
from .forms import LivreForm, CdForm, DvdForm, JeuxDePlateauForm

# Create your views here.


def accueil_bibliothecaire(request):

    context = {"livre" : Livre.objects.all(),
               "dvd" : Dvd.objects.all(),
               "cd" : Cd.objects.all(),
               "jeux_de_plateau" : Jeux_de_plateau.objects.all(),
               }
    
    return render(request, 'accueil_bibliothecaire.html', context)

#----------------------------- Partie Livre --------------------------------

def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
        
    else:
        form = LivreForm()
    
    return render(request, 'ajouter_livre.html', {'form':form})


def modifier_livre(request, livre_id):
    livre = get_object_or_404(Livre, id = livre_id)

    if request.method == 'POST':
        form = LivreForm(request.POST, instance = livre)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
        
    else:
        form = LivreForm(instance = livre)
    
    return render(request, 'modifier_livre.html', {'form':form, 'livre':livre})


def supprimer_livre(request, livre_id):
    livre = get_object_or_404(Livre, id = livre_id)

    if request.method == 'POST':
        livre.delete()
        return redirect("bibliothecaire:accueil_bibliothecaire")
    
    return render(request, 'supprimer_livre.html', {'livre':livre})

#-------------- fin de partie livre -----------------------------------

#-------------------- Partie cd ---------------------------------------

def ajouter_cd(request):
    if request.method == 'POST':
        form = CdForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
        
    else:
            form = CdForm()

    return render(request, 'ajouter_cd.html', {'form':form})


def modifier_cd(request, cd_id):
    cd = get_object_or_404(Cd, id = cd_id)

    if request.method == 'POST':
        form = CdForm(request.POST, instance = cd)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
        
    else:
        form = CdForm(instance = cd)

    return render(request, 'modifier_cd.html', {'form':form, 'cd':cd})


def supprimer_cd(request, cd_id):
    cd = get_object_or_404(Cd, id = cd_id)

    if request.method == 'POST':
        cd.delete()
        return redirect("bibliothecaire:accueil_bibliothecaire")
    
    return render(request, 'supprimer_cd.html', {'cd':cd})

#----------------------- fin de partie cd ------------------------------

#------------------------ partie dvd -------------------------------------

def ajouter_dvd(request):
    if request.method == 'POST':
        form = DvdForm(request)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
    
    else:
        form = DvdForm()
    
    return render(request, 'ajouter_dvd.html', {'form':form})


def modifier_dvd(request, dvd_id):
    dvd = get_object_or_404(Dvd, id = dvd_id)

    if request.method == 'POST':
        form = DvdForm(request.POST, instance = dvd)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
        
    else:
        form = DvdForm(instance = dvd)

    return render(request, 'modifier_dvd.html', {'form':form, 'dvd':dvd})


def supprimer_dvd(request, dvd_id):
    dvd = get_object_or_404(Dvd, id = dvd_id)

    if request.method == 'POST':
        dvd.delete()
        return redirect("bibliothecaire:accueil_bibliothecaire")
    
    return render(request, 'supprimer_dvd.html', {'dvd':dvd})

#-----------------fin de partie dvd ---------------------------------------

#-----------------------partie jeux de plateaux ----------------------------

def ajouter_jeux_de_plateau(request):
    if request.method == 'POST':
        form = JeuxDePlateauForm(request)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
    
    else:
        form = JeuxDePlateauForm()
    
    return render(request, 'ajouter_jeux_de_plateau.html', {'form':form})


def modifier_jeux_de_plateau(request, jeux_de_plateau_id):
    jeux_de_plateau = get_object_or_404(Jeux_de_plateau, id = jeux_de_plateau_id)

    if request.method == 'POST':
        form = JeuxDePlateauForm(request.POST, instance = jeux_de_plateau)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
        
    else:
        form = JeuxDePlateauForm(instance = jeux_de_plateau)

    return render(request, 'modifier_jeux_de_plateau.html', {'form':form, 'jeux_de_plateau':jeux_de_plateau})


def supprimer_jeux_de_plateau(request, jeux_de_plateau_id):
    jeux_de_plateau = get_object_or_404(Jeux_de_plateau, id = jeux_de_plateau_id)

    if request.method == 'POST':
        jeux_de_plateau.delete()
        return redirect("bibliothecaire:accueil_bibliothecaire")
    
    return render(request, 'supprimer_jeux_de_plateau.html', {'jeux_de_plateau':jeux_de_plateau})