from PIL import Image

imagem = Image.open('starWars.png')
imagemGray = imagem.convert('L')
imagemGray.save('starWarsGray.png')
