from django.urls import path
from . import views


app_name = 'bibliothecaire'

urlpatterns = [
    path('accueil', views.accueil_bibliothecaire, name = 'accueil_bibliothecaire'),
    path('ajout_livre', views.ajout_livre, name = 'ajout_livre'),
    path('modifier_livre/<int:livre_id>/', views.modifier_livre, name = 'modifier_livre'),
    path('supprimer_livre/<int:livre_id>/', views.supprimer_livre, name = 'supprimer_livre')
]