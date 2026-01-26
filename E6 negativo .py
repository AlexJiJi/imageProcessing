from PIL import Image


def Negativo(im):
    n,m = im.size
    modelo = im.mode
    negativo = Image.new(modelo,(n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            nr = 255 - r
            ng = 255 - g
            nb = 255 - b
            pixel = tuple([nr,ng,nb])
            negativo.putpixel((i,j), pixel)
            j += 1
        i += 1
    negativo.save("negativo.jpg")
    return negativo
    
ruta = "baboon.jpg"
im = Image.open(ruta)
im = Negativo(im)
im.show() 








