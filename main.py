import cv2
import pytesseract
import joblib  # Pour charger le modèle pré-entrainé

# Configurez le chemin d'installation de Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Charger le modèle pré-entrainé
model = joblib.load('trained_model.joblib')

# Initialiser la webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()  # Lire l'image de la webcam
    if not ret:
        break

    # Prétraitement et extraction de texte
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    text = pytesseract.image_to_string(gray, config='--oem 3 --psm 6')

    # Prédiction de la classification
    prediction = model.predict([text])

    # Afficher le texte et le résultat de la prédiction
    cv2.putText(frame, f'Texte: {text}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    cv2.putText(frame, f'Classification: {prediction[0]}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Afficher le flux vidéo avec les résultats
    cv2.imshow("Détection de contenu politique", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
