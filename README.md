# MEDIATHEQUE
Projet développé avec Django.

## POUR INSTALLER LE PROJET
### 1. Cloner le projet
Dans le terminal d'un nouveau dossier entrer la commande :\
``` git clone https://github.com/julien696/mediatheque.git``` 
``` cd mediatheque```

### 2. Créer un environement virtuel
``` python -m venv env```
Puis activer.\
Sous Windows :\
``` env\Scripts\activate```\
Sous Mac/Linux :\
``` source env/bin/activate```

### 3. Installer les dépendance
``` pip install -r requirements.txt```

### 4. Appliquer les migrations
``` python manage.py migrate```

### 5. Créer un super utilisateur (Accés blibliothécaire)
``` python manage.py createsuperuser```

### 6. Lancer le serveur
``` python manage.py runserver```

### 7. Lancer les test
``` python manage.py test```