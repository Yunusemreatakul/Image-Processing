import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('images/manzara.jpg')
normalized_image = image / 255.0

gamma = 1.5
gamma_corrected = np.power(normalized_image, gamma)

gamma_corrected = np.uint8(gamma_corrected * 255.0)

plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(gamma_corrected, cv2.COLOR_BGR2RGB))
plt.title('Gamma Düzeltme (γ=1.5)')
plt.axis('off')

plt.tight_layout()
plt.show()
