import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('images/manzara.jpg', cv2.IMREAD_GRAYSCALE)


kernel = np.ones((5,5), np.uint8)


opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)


closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)


plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.imshow(image, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(opening, cmap='gray')
plt.title('Açma İşlemi')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(closing, cmap='gray')
plt.title('Kapama İşlemi')
plt.axis('off')

plt.tight_layout()
plt.show()
