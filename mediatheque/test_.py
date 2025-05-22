import pytest
from django.contrib.auth.models import User
from django.urls import reverse


@pytest.mark.django_db
def test_connexion_superuser_success(client):
    superuser = User.objects.create_superuser(username='admin', password='1234', email='admin@gmail.com')

    reponse = client.post(reverse('connexion_superuser'), {'username': 'admin', 'password': '1234'})

    assert reponse.status_code == 302
    assert reponse.url == reverse('bibliothecaire:accueil_bibliothecaire')

@pytest.mark.django_db
def test_connexion_superuser_invalid_user(client):
    response = client.post(reverse('connexion_superuser'), {
        'username': 'wrong',
        'password': 'wrongpass',
    })

    assert response.status_code == 200
    assert b'Identifiant invalide' in response.content