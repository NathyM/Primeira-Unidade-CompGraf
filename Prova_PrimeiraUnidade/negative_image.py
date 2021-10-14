import cv2
import matplotlib.pyplot as plt

img = cv2.imread('starWarsGray.png', 1)


#Coleta dos canais diferentes - 3 canais em cada pixel
#separação de cada canal em uma variavel diferente
#negar o valor de cada pixel e armazenar substituindo o anterior

height, width, _ = img.shape

for i in range(0, height - 1):
    for j in range(0, width - 1):
        pixel = img[i, j]

        pixel[0] = 255 - pixel[0]

        pixel[1] = 255 - pixel[1]

        pixel[2] = 255 - pixel[2]

        img[i, j] = pixel
plt.imshow(img)
plt.show()

