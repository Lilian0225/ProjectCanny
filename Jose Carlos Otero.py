import cv2
import pydicom
import matplotlib.pyplot as plt


imagen_dicom = pydicom.dcmread('0020.DCM')
pixeles = imagen_dicom.pixel_array[0]
canny = cv2.Canny(pixeles, 50, 100)

plt.subplot(121), plt.imshow(pixeles, cmap='gray')
plt.title('Imagen original'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(canny, cmap='gray')
plt.title('Algoritmo de Canny'), plt.xticks([]), plt.yticks([])
plt.show()
