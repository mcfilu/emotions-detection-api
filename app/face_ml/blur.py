from io import BytesIO
from mtcnn import MTCNN
import numpy as np
import cv2
import tensorflow as tf

"""
* This part is set to be processed only by the CPU. 
"""
tf.config.set_visible_devices([], 'GPU')


def apply_blur(image, depth):
    detector = MTCNN()

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = detector.detect_faces(image)
    for face in faces:
        x, y, w, h = face['box']
        face = image[y:y + h, x:x + w]
        blurred_face = cv2.GaussianBlur(face, (47, 47), depth)
        mask = np.zeros_like(face)
        cv2.circle(mask, (w // 2, h // 2), min(w, h) // 2, (255, 255, 255), -1)
        face[np.where(mask)] = blurred_face[np.where(mask)]
        image[y:y + h, x:x + w] = face

    return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
