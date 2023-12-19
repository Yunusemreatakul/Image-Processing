import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('images/manzara.jpg', cv2.IMREAD_GRAYSCALE)


blurred_image = cv2.GaussianBlur(image, (3, 3), 0)


laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)


plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplace Operatörü ile Kenar Tespiti')
plt.axis('off')

plt.tight_layout()
plt.show()
