import cv2
import matplotlib.pyplot as plt

image = cv2.imread('images/manzara.jpg', cv2.IMREAD_GRAYSCALE)


equalized_image = cv2.equalizeHist(image)


plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Histogram Görüntü')
plt.axis('off')

plt.tight_layout()
plt.show()
