import cv2

# Carrega o modelo pré-treinado de detecção de faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Abre a webcam
cap = cv2.VideoCapture(0)

while True:
    # Lê o frame da webcam
    ret, frame = cap.read()

    # Converte o frame para escala de cinza
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detecta faces no frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Desenha retângulos ao redor das faces detectadas
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Salva a face detectada com um nome e formato de arquivo específico
        face_name = "new_face"
        face_file = f"{face_name}.jpg"  # or f"{face_name}.png"
        cv2.imwrite(face_file, frame[y:y+h, x:x+w])

    # Exibe o frame com as faces detectadas
    cv2.imshow('Detecção de Faces', frame)

    # Interrompe o loop se a tecla 'q' for pressionada
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a webcam e fecha a janela
cap.release()
cv2.destroyAllWindows()
