import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
import joblib
import string

# Charger les données d'entraînement
df = pd.read_csv('data/training_data.csv')

# Fonction pour prétraiter le texte
def preprocess_text(text):
    # Convertir en minuscules
    text = text.lower()
    # Supprimer la ponctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Appliquer le prétraitement sur la colonne 'text'
df['text'] = df['text'].apply(preprocess_text)

# Pipeline pour le modèle
stop_words = ['et', 'le', 'la', 'à', 'de', 'les', 'des', 'un', 'une', 'pour', 'dans', 'est', 'ce', 'que']  # Liste des stop words en français
model = make_pipeline(CountVectorizer(stop_words=stop_words), MultinomialNB())

# Entraîner le modèle
model.fit(df['text'], df['label'])

# Sauvegarder le modèle
joblib.dump(model, 'trained_model.joblib')
