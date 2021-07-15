import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("Wakanda.jpg",0)
ret, threst = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
kernel = np.ones((5,5),np.uint8)
dilasi = cv2.dilate(threst,kernel,iterations=1)

plt.subplot(131),plt.imshow(img,cmap='gray')
plt.title('Awal'), plt.xticks([]), plt.yticks([])
plt.subplot(132), plt.imshow(threst,cmap='gray')
plt.title('Biner'), plt.xticks([]), plt.yticks([])
plt.subplot(133), plt.imshow(dilasi,cmap='gray')
plt.title('Dilasi'), plt.xticks([]),plt.yticks([])
plt.show()