# MEDIATHEQUE
Projet développé avec Django.

## POUR INSTALLER LE PROJET
### 1. Cloner le projet
Dans le terminal d'un nouveau dossier entrer la commande :\
``` git clone https://github.com/julien696/mediatheque.git``` 
``` cd mediatheque```

### 2. Créer un environnement virtuel
``` python -m venv env```
Puis activer.\
Sous Windows :\
``` env\Scripts\activate```\
Sous Mac/Linux :\
``` source env/bin/activate```

### 3. Installer les dépendances
``` pip install -r requirements.txt```

### 4. Appliquer les migrations
``` python manage.py migrate```

### 5. Charger les fixtures
```python manage.py loaddata medias.json ```

### 6. Créer un super utilisateur (Accès blibliothécaire)
``` python manage.py createsuperuser```

### 7. Lancer le serveur
``` python manage.py runserver```

### 8. Lancer les tests
``` python manage.py test```
