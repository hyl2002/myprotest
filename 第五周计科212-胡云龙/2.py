import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('house.png', 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)
dft_shift[122:131, 0:125] = 255
dft_shift[122:131, 131:256] = 255
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()
f_ishif = np.fft.ifftshift(dft_shift)
img_back = cv2.idft(f_ishif)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
# img_back=cv2.medianBlur(img_back,(3,3),5)
plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(img_back, cmap='gray')
plt.title('Result'), plt.xticks([]), plt.yticks([])
plt.show()
