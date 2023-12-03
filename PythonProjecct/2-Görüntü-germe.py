import cv2
import numpy as np
img = cv2.imread('images/manzara.jpg', cv2.IMREAD_GRAYSCALE)


min_val = np.min(img)
max_val = np.max(img)
linear_stretched = (img - min_val) / (max_val - min_val) * 255


alpha = 1.5
beta = 0
contrast_stretched = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)


cv2.imshow('Orjinal Goruntu', img)
cv2.imshow('Doğrusal Germe', linear_stretched)
cv2.imshow('Kontrast Germe', contrast_stretched)
cv2.waitKey(0)
cv2.destroyAllWindows()