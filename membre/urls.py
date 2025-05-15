from django.urls import path
from membre.views import accueil_membre


app_name = 'membre'


urlpatterns = [
    path('accueil/', accueil_membre, name = 'accueil_membre')
]