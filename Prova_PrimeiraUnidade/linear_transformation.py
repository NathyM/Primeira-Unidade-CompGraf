import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('starWarsGray.png')

def transformacao_linear(imagem, g_min, g_max):
  f_min = min(imagem.flatten())
  f_max = max(imagem.flatten())
  a = (g_max - g_min) / (f_max - f_min)
  b = g_min
  imagem = imagem - f_min
  nova_imagem = (a*imagem) + b
  return np.uint8(nova_imagem)

new_imagem = transformacao_linear(imagem,20,100)
cv2.imshow('imagem', new_imagem)
cv2.waitKey(0)

#histograma da nova imagem
histogram = cv2.calcHist([new_imagem],[0],None,[256],[0,256])
plt.title("Histograma")
plt.grid(True)
plt.plot(histogram)
plt.show()