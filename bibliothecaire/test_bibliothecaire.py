import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Livre, Membre, Emprunt
from django.utils import timezone
from datetime import date, timedelta


@pytest.fixture
def superuser(client):
    user = User.objects.create_superuser(username='admin', password='1234', email='admin@example.com')
    client.login(username='admin', password='1234')
    return client


@pytest.mark.django_db
def test_accueil(superuser):
    url = reverse('bibliothecaire:accueil_bibliothecaire')
    response = superuser.get(url)

    assert response.status_code == 200
    assert "accueil_bibliothecaire.html" in [t.name for t in response.templates]
    assert "livres" in response.context
    assert "dvds" in response.context
    assert "cds" in response.context
    assert "jeux_de_plateau" in response.context
    assert "membres" in response.context
    assert "emprunts" in response.context


@pytest.mark.django_db
def test_ajout_livre(superuser):
    url = reverse('bibliothecaire:ajouter_livre')
    data = {'nom': 'Le Petit Prince', 'auteur': 'Antoine de Saint-Exupéry'}
    response = superuser.post(url, data)

    assert response.status_code == 302 
    assert Livre.objects.filter(nom = 'Le Petit Prince').exists()



@pytest.mark.django_db
def test_affichage_form_ajout_livre(superuser):
    url = reverse('bibliothecaire:ajouter_livre')

    response = superuser.get(url)

    assert response.status_code == 200
    assert '<form' in response.content.decode()



@pytest.mark.django_db
def test_modifier_livre(superuser):
    livre = Livre.objects.create(nom='ancien', auteur='ancien')
    url = reverse('bibliothecaire:modifier_livre', kwargs={'livre_id': livre.id})
    data = {'nom':'nouveau_livre', 'auteur':'nouveau_auteur'}
    
    response = superuser.post(url, data)
    livre.refresh_from_db()

    assert response.status_code == 302
    assert livre.nom == 'nouveau_livre'
    assert livre.auteur == 'nouveau_auteur'



@pytest.mark.django_db
def test_suprimer_livre(superuser):
    livre = Livre.objects.create(nom='livre', auteur='auteur')
    url = reverse('bibliothecaire:supprimer_livre', kwargs={'livre_id': livre.id})

    response = superuser.post(url)

    assert response.status_code == 302
    assert not Livre.objects.filter(id=livre.id).exists()



@pytest.mark.django_db
def test_liste_livre(superuser):
    livre = Livre.objects.create(nom='livre', auteur='livre')
    url = reverse('bibliothecaire:liste_livre')

    response = superuser.get(url)

    assert response.status_code == 200
    assert 'livre' in response.content.decode()



@pytest.mark.django_db
def test_emprunt_media(superuser):
    livre = Livre.objects.create(nom='livre', auteur='livre')
    membre = Membre.objects.create(nom='Doe', prenom='John')
    url = reverse('bibliothecaire:emprunter_media', args=['livres', livre.id])
    data = { 'membre':membre.id}

    response = superuser.post(url, data)

    assert response.status_code == 200
    assert 'Emprunt/confirmation_emprunt.html' in [t.name for t in response.templates]
    
    livre.refresh_from_db()
    assert livre.disponible is False
    
    emprunt = Emprunt.objects.filter(membre=membre, livre_emprunt=livre).first()
    assert emprunt is not None
    assert emprunt.date_emprunt == timezone.now().date()
    assert emprunt.date_retour == emprunt.date_emprunt + timedelta(days=7)



@pytest.mark.django_db
def test_limite_emprunt(superuser):
    membre = Membre.objects.create(nom = 'Doe', prenom = 'John')
    for i in range(3):
        livre = Livre.objects.create(nom = f"Livre {i}", auteur =  f'auteur {i}')
        Emprunt.objects.create(membre = membre, livre_emprunt = livre, date_emprunt=timezone.now().date(), date_retour=timezone.now().date() + timedelta(days=7))
        livre.save()

    nouveau_livre = Livre.objects.create(nom = "nouveau", auteur = "nouveau")
    url = reverse('bibliothecaire:emprunter_media', args=['livres', nouveau_livre.id])

    response = superuser.post(url, data={'membre':membre.id})

    assert response.status_code == 200
    assert 'Emprunt/limite_emprunt.html' in [t.name for t in response.templates]



@pytest.mark.django_db
def test_Emprunt_en_retard(superuser):
    membre = Membre.objects.create(nom = 'Doe', prenom = 'John')
    livre_retard = Livre.objects.create(nom = "livre_retard", auteur = "auteur")
    Emprunt.objects.create(membre = membre,
                           livre_emprunt = livre_retard,
                           date_emprunt = timezone.now().date() - timedelta(days=10),
                           date_retour = timezone.now().date() - timedelta(days=3))
    livre_retard.save()

    nouveau_livre = Livre.objects.create(nom = "nouveau", auteur = "nouveau")
    url = reverse('bibliothecaire:emprunter_media', args=['livres', nouveau_livre.id])

    response = superuser.post(url, data={'membre':membre.id})

    assert response.status_code == 200
    assert 'Emprunt/emprunt_en_retard.html' in [t.name for t in response.templates]

