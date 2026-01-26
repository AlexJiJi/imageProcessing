from PIL import Image


def escala_grises(im):
    n, m = im.size
    modelo = im.mode
    escala_gris = Image.new(modelo,(n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            gris = (r+g+b)/3
            gris = round(gris)
            pixel = tuple([gris,gris,gris])
            escala_gris.putpixel((i,j),pixel)
            j+=1
        i+=1
    return escala_gris


def extraerRojo(im):
    n,m = im.size
    imgris = escala_grises(im)
    i = 0
    while i < n:
        j = 0
        while j < m:
            r, g, b = im.getpixel((i,j))
            if r > g+b:
                pixel = tuple([r,g,b])
                imgris.putpixel((i,j), pixel)
            j +=1
        i += 1
    imgris.save("Rojoextract.png")
    return imgris


ruta = "pepper.jpg"
im = Image.open(ruta)
im = extraerRojo(im)
im.show()