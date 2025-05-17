from django import forms
from .models import Livre, Dvd, Cd, Jeux_de_plateau


class LivreForm(forms.ModelForm):

    class Meta:
        model = Livre
        fields = ['nom', 'auteur']
        labels = {'nom': 'Titre', 'auteur': 'Auteur'}


class DvdForm(forms.ModelForm):

    class Meta:
        model = Dvd
        fields = ['nom', 'realisateur']
        labels = {'nom': 'Titre', 'realisateur': 'Réalisateur'}


class CdForm(forms.ModelForm):

    class Meta:
        model = Cd
        fields = ['nom', 'artiste']
        labels = {'nom': 'Titre', 'artiste': 'Artiste'}


class JeuxDePlateauForm(forms.ModelForm):

    class Meta:
        model = Jeux_de_plateau
        fields = ['nom', 'createur']
        labels = {'nom': 'Nom', 'createur': 'Créateur'}