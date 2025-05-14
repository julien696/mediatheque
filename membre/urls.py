from django.urls import path
from membre.views import liste_medias


app_name = 'membre'


urlpatterns = [
    path('', liste_medias, name = 'liste_medias')
]