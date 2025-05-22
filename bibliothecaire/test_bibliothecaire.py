import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Livre


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
