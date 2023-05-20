import cv2
import numpy as np


class Camera:
    def __init__(self) -> None:
        self.video = cv2.VideoCapture(0)

    def capture(self) -> np.ndarray:
        ret, frame = self.video.read()
        if not ret:
            raise Exception("Could not read video frame")
        else:
            return frame

    def close(self):
        self.video.release()
        cv2.destroyAllWindows()

      
