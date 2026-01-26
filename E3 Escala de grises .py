from PIL import Image

def escala_grises(im):
    n = im.size[0]
    m = im.size[1]
    modelo = im.mode
    escala_gris = Image.new(modelo,(n,m)) #escala_gris = Image.new('L',(n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            gris = (r+g+b)/3
            gris = round(gris)
            pixel = tuple([gris,gris,gris]) #gris
            escala_gris.putpixel((i,j),pixel)
            j+=1
        i+=1
    escala_gris.save("img_gris2.jpg")
    return escala_gris

ruta = "baboon.jpg"
im = Image.open(ruta)
im = escala_grises(im)
im.show() 