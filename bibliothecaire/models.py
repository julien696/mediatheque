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


class Emprunt(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE)
    livre_emprunt = models.ForeignKey(Livre, on_delete=models.SET_NULL, null=True, blank=True)
    cd_emprunt = models.ForeignKey(Cd, on_delete=models.SET_NULL, null=True, blank=True)
    dvd_emprunt = models.ForeignKey(Dvd, on_delete=models.SET_NULL, null=True, blank=True)
    date_emprunt = models.DateField(auto_now=True)
    date_retour = models.DateField()
    date_retour_effectif = models.DateField(null=True, blank=True)

    def __str__(self):
        media = self.livre_emprunt or self.cd_emprunt or self.dvd_emprunt
        return f"{self.membre} a emprunté {media} le {self.date_emprunt}"