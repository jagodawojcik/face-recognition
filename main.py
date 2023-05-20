import cv2
from camera import Camera
from face_recognition import FaceRecognition

if __name__ == "__main__":
    camera = Camera()
    face_cascade = FaceRecognition()

    while True:
        frame = camera.capture()

        # Detect faces in the frame
        face_cascade.detect_faces(frame)

        # Wait for a key press
        if cv2.waitKey(1) == 27:
            break

    camera.close()
