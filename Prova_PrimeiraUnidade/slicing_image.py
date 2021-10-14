import  cv2

imagem = cv2.imread('starWars.png')
slicing_image = cv2.rectangle(imagem, (0, 0), ((imagem.shape[1]//3), imagem.shape[0]), (0, 0, 0), -1)
cv2.imshow('imagem ', slicing_image)
cv2.imwrite('starWars_sliced.png', slicing_image)
cv2.waitKey(0)