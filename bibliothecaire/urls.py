from django.urls import path
from . import views


app_name = 'bibliothecaire'

urlpatterns = [
    path('accueil', views.accueil_bibliothecaire, name = 'accueil_bibliothecaire'),
    
    #-----------------------Livre-----------------------------------------------
    path('ajouter_livre', views.ajouter_livre, name = 'ajouter_livre'),
    path('modifier_livre/<int:livre_id>/', views.modifier_livre, name = 'modifier_livre'),
    path('supprimer_livre/<int:livre_id>/', views.supprimer_livre, name = 'supprimer_livre'),
    path('liste_livre', views.liste_livre, name = 'liste_livre'),


    #-------------------------cd-----------------------------------------------
    path('ajouter_cd', views.ajouter_cd, name = 'ajouter_cd'),
    path('modifier_cd/<int:cd_id>/', views.modifier_cd, name = 'modifier_cd'),
    path('supprimer_cd/<int:cd_id>/', views.supprimer_cd, name = 'supprimer_cd'),
    path('liste_cd', views.liste_cd, name = 'liste_cd'),


    #------------------------------dvd--------------------------------------------
    path('ajouter_dvd', views.ajouter_dvd, name = 'ajouter_dvd'),
    path('modifier_dvd/<int:dvd_id>/', views.modifier_dvd, name = 'modifier_dvd'),
    path('supprimer_dvd/<int:dvd_id>/', views.supprimer_dvd, name = 'supprimer_dvd'),
    path('liste_dvd', views.liste_dvd, name = 'liste_dvd'),


    #-----------------------------jeux_de_plateau------------------------------------
    path('ajouter_jeux_de_plateau', views.ajouter_jeux_de_plateau, name = 'ajouter_jeux_de_plateau'),
    path('modifier_jeux_de_plateau/<int:jeux_de_plateau_id>/', views.modifier_jeux_de_plateau, name = 'modifier_jeux_de_plateau'),
    path('supprimer_jeux_de_plateau/<int:jeux_de_plateau_id>/', views.supprimer_jeux_de_plateau, name = 'supprimer_jeux_de_plateau'),
    path('liste_jeux', views.liste_jeux, name = 'liste_jeux'),
    
    
    #------------------------------membre------------------------------------------
    path('ajouter_membre', views.ajouter_membre, name = 'ajouter_membre'),
    path('modifier_membre/<int:membre_id>/', views.modifier_membre, name = 'modifier_membre'),
    path('supprimer_membre/<int:membre_id>/', views.supprimer_membre, name = 'supprimer_membre'),
    path('liste_membre', views.liste_membre, name = 'liste_membre'),


    #-------------------------------emprunt--------------------------------------------------
    path('emprunter/<str:media_type>/<int:media_id>/', views.emprunter_media, name = 'emprunter_media'),
    path('confirmation_emprunt', views.confirmation_emprunt, name = 'confirmation_emprunt'),
    path('limite_emprunt', views.limite_emprunt, name = 'limite_emprunt'),
    path('emprunt_en_retard', views.emprunt_en_retard, name = 'emprunt_en_retard'),
    path('rendre_emprunt/<int:emprunt_id>/', views.rendre_emprunt, name ='rendre_emprunt'),
    path('liste_emprunt', views.liste_emprunt, name = 'liste_emprunt')
]