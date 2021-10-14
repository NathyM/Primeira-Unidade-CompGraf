import cv2
from matplotlib import pyplot as plt

imagem = cv2.imread('starWarsGray.png',0)
histogram = cv2.calcHist([imagem],[0],None,[256],[0,256])
plt.title("Histograma")
plt.grid(True)
plt.plot(histogram)
plt.show()
