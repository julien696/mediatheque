"""
URL configuration for mediatheque project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mediatheque.views import accueil, connexion_superuser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueil, name = 'accueil'),
    path('connexion_superuser', connexion_superuser, name = 'connexion_superuser'),
    path('membre/', include('membre.urls')),
    path('bibliothecaire/', include('bibliothecaire.urls'))
]
