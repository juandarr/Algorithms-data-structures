import cv2 
from matplotlib import pyplot as plt

flowers = cv2.imread('flowers.jpg')
flowers = cv2.cvtColor(flowers, cv2.COLOR_BGR2RGB)
flowers_lab = cv2.cvtColor(flowers, cv2.COLOR_RGB2LAB)
flowers_yuv = cv2.cvtColor(flowers, cv2.COLOR_RGB2YUV)

print(flowers_lab.shape)

plt.figure(1)
plt.subplot(131)
plt.title('RGB color space')
plt.imshow(flowers)

plt.subplot(132)
plt.title('LAB color space')
plt.imshow(flowers_lab)

plt.subplot(133)
plt.title('YUV color space')
plt.imshow(flowers_yuv)
plt.show()