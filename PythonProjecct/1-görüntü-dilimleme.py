import cv2
import numpy as np

img = cv2.imread('images/200tl.jpg', cv2.IMREAD_GRAYSCALE)
lower_threshold = 60
upper_threshold = 120
binary = np.zeros_like(img)
binary[(img > lower_threshold) & (img < upper_threshold)] = 255
cv2.imshow('Orijinal Goruntu', img)
cv2.imshow('Dilimlenmis Goruntu', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
