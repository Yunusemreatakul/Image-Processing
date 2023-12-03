import cv2
import numpy as np


image = cv2.imread('images/200tl.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gaussian_kernel = cv2.getGaussianKernel(5, 1)
gaussian_filter = np.outer(gaussian_kernel, gaussian_kernel.transpose())

filtered_image = cv2.filter2D(gray_image, -1, gaussian_filter)

cv2.imshow('Orijinal Görüntü', gray_image)
cv2.imshow('Gauss Filtre Uygulanmış Görüntü', filtered_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
