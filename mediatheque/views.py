from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def accueil(request):
    return render(request, "base.html")


def connexion_superuser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('bibliothecaire:accueil_bibliothecaire')
        
        else:
            messages.error(request, 'Identifiant invalide')
    
    return render(request, 'connexion_superuser.html')