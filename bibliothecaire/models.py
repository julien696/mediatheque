from django.db import models


# Create your models here.


class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} - {self.prenom}"


class Emprunteur(models.Model):
    nom = models.CharField(max_length=100)
    bloque = models.BooleanField(default=False)

    def __str__(self):
        return self.nom


class Media(models.Model):
    nom = models.CharField(max_length=100)
    date_emprunt = models.DateField(null=True, blank=True)
    disponible = models.BooleanField(default=True)
    emprunteur = models.ForeignKey(Emprunteur, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        abstract = True


class Livre(Media):
    auteur = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} - {self.auteur}"


class Dvd(Media):
    realisateur = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} - {self.realisateur}"


class Cd(Media):
    artiste = models.CharField(max_length=100)

    def __str_(self):
        return f"{self.nom} - {self.artiste}"


class Jeux_de_plateau(models.Model):
    nom = models.CharField(max_length=100)
    createur = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} - {self.createur}"


