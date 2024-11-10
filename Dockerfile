# Utiliser une image Python 3.11
FROM python:3.11

# Définir le répertoire de travail
WORKDIR /code

# Copier le fichier requirements.txt dans le conteneur
COPY ./requirements.txt /code/requirements.txt

# Installer les dépendances Python, y compris Uvicorn
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copier le code source dans le conteneur
COPY . /code

# Démarrer l’application avec Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
