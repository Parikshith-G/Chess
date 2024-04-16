from PIL import Image


x,y,u,d=320,00,350,00

image=Image.open('pieces.png')
king=(30+x,30+y,300+u,300+d)
piece_image=image.crop(king)
piece_image.save('white_queen.png')
piece_image.save('a.png')