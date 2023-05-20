import cv2
import numpy as np

class FaceRecognition:
    def __init__(self) -> None:
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    def detect_faces(self, frame: np.ndarray) -> None:
        grayscale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.face_cascade.detectMultiScale(grayscale_image, scaleFactor=1.1, minNeighbors=5)

        for face in faces:
            cv2.rectangle(frame, face, (0, 255, 0), 2)

        cv2.imshow('Face Recognition', frame)
