from django.shortcuts import render, redirect, get_object_or_404
from .models import Livre, Cd, Dvd, Jeux_de_plateau, Membre, Emprunt
from .forms import LivreForm, CdForm, DvdForm, JeuxDePlateauForm, MembreForm, EmprunterMediaForm
from datetime import date, timedelta
from django.utils import timezone
from django.contrib import messages

# Create your views here.


def accueil_bibliothecaire(request):

    context = {"livres" : Livre.objects.all(),
               "dvds" : Dvd.objects.all(),
               "cds" : Cd.objects.all(),
               "jeux_de_plateau" : Jeux_de_plateau.objects.all(),
               "membres" : Membre.objects.all(),
               "emprunts": Emprunt.objects.all().select_related('membre', 'livre_emprunt', 'dvd_emprunt', 'cd_emprunt')
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
        form = DvdForm(request.POST)

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
        form = JeuxDePlateauForm(request.POST)

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

#--------------------------Fin de partie jeux de plateau -----------------------------------

#------------------------------ partie Membre ------------------------------------------

def ajouter_membre(request):
    if request.method == 'POST':
        form = MembreForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
        
    else:
        form = MembreForm()

    return render(request, 'ajouter_membre.html', {'form':form})


def modifier_membre(request, membre_id):
    membre = get_object_or_404(Membre, id = membre_id)

    if request.method == 'POST':
        form = MembreForm(request.POST, instance = membre)

        if form.is_valid():
            form.save()
            return redirect("bibliothecaire:accueil_bibliothecaire")
        
    else:
        form = MembreForm(instance = membre)

    return render(request, 'modifier_membre.html', {'form':form, 'membre':membre})


def supprimer_membre(request, membre_id):
    membre = get_object_or_404(Membre, id = membre_id)

    if request.method == 'POST':
        membre.delete()
        return redirect("bibliothecaire:accueil_bibliothecaire")
    
    else:
        return render(request, 'supprimer_membre.html', {'membre':membre})
    

def emprunter_media(request, media_type, media_id):
    if media_type == 'livres':
        media = get_object_or_404(Livre, pk=media_id)

    elif media_type == 'dvds':
        media = get_object_or_404(Dvd, pk=media_id)

    elif media_type == 'cds':
        media =get_object_or_404(Cd, pk=media_id)

    else:
        messages.warning(request, 'Le média est inconnue')
        return redirect("bibliothecaire:accueil_bibliothecaire")
    
    if not media.disponible:
        messages.warning(request, 'Le média est indisponible')
        return redirect("bibliothecaire:accueil_bibliothecaire")
    

    if request.method == 'POST':
        form = EmprunterMediaForm(request.POST)
        if form.is_valid():
            membre = form.cleaned_data['membre']

        # Vérification du nombre d'emprunt
            emprunts_actifs = Emprunt.objects.filter(membre = membre, date_retour_effectif__isnull=True).count()
            if emprunts_actifs >= 3 :
                return render(request, 'limite_emprunt.html', {'membre':membre})
            
            # Vérification des emprunts en retard
            emprunt_en_retard = Emprunt.objects.filter(membre = membre, date_retour_effectif__isnull=True, date_retour__lt = date.today())
            if emprunt_en_retard.exists():
                return render(request, 'emprunt_en_retard.html', {'membre':membre})
        
            
            # Création de l'emprunt
            date_emprunt = timezone.now().date()
            date_retour = date_emprunt + timedelta(days=7)

            if media_type == 'livres':
                Emprunt.objects.create(membre = membre, livre_emprunt = media, date_emprunt = date_emprunt, date_retour = date_retour)
            
            elif media_type == 'dvds':
                Emprunt.objects.create(membre = membre, dvd_emprunt = media, date_emprunt = date_emprunt, date_retour = date_retour)

            elif media_type == 'cds':
                Emprunt.objects.create(membre = membre, cd_emprunt = media, date_emprunt = date_emprunt, date_retour = date_retour)

            media.disponible = False
            media.save()
            return render(request, 'confirmation_emprunt.html', {'media':media, 'membre':membre})

    else:
        form = EmprunterMediaForm()

    membres = Membre.objects.all()
    return render(request, 'emprunter_media.html', {'form':form, 'media_type':media_type, 'media_id':media_id, 'membres':membres})


def confirmation_emprunt(request):
    return render(request, 'confirmation_emprunt.html')


def limite_emprunt(request):
    return render(request, 'limite_emprunt.html')


def emprunt_en_retard(request):
    return render(request, 'emprunt_en_retard.html')


def rendre_emprunt(request, emprunt_id):
    emprunt = get_object_or_404(Emprunt, pk=emprunt_id)

    if emprunt.date_retour_effectif is None:
        emprunt.date_retour_effectif = date.today()
        emprunt.save()

        if emprunt.livre_emprunt:
            emprunt.livre_emprunt.disponible = True
            emprunt.livre_emprunt.save()

        elif emprunt.cd_emprunt:
            emprunt.cd_emprunt.disponible = True
            emprunt.cd_emprunt.save()

        elif emprunt.dvd_emprunt:
            emprunt.dvd_emprunt.disponible = True
            emprunt.dvd_emprunt.save()

        messages.success(request, "L'emprunt est retourné.")
    
    else:
        messages.warning(request, "Cet emprunt a déjà été retourné.")
    
    return redirect('bibliothecaire:accueil_bibliothecaire')


