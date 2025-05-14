from django.db import models


# Create your models here.


class Emprunteur(models.Model):
    nom = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)


class Media(models.Model):
    nom = models.CharField(max_length=100)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True


class Livre(Media):
    auteur = models.CharField(max_length=100)


class Dvd(Media):
    realisateur = models.CharField(max_length=100)


class Cd(Media):
    artiste = models.CharField(max_length=100)


class Jeux_de_plateau(models.Model):
    nom = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)