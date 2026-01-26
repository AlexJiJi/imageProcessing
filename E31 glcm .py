from PIL import Image
from matplotlib import pyplot as plt

def escala_grises(im):
    n = im.size[0]
    m = im.size[1]
    escala_gris = Image.new('L',(n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            gris = (r+g+b)/3
            gris = round(gris)
            pixel = gris
            escala_gris.putpixel((i,j),pixel)
            j+=1
        i+=1
    return escala_gris

def glcm(im):
    im = escala_grises(im)
    hist = []
    G = 256
    for n in range(65536):
        hist.append(0)
    n,m = im.size
    i = 1
    while i < n - 1:
        j = i
        while j < m - 1:
            glmc0 = G * im.getpixel((i,j)) + im.getpixel((i,i+1))
            glmc1 = G * im.getpixel((i,j)) + im.getpixel((i-1,j+1))
            glmc2 = G * im.getpixel((i,j)) + im.getpixel((i-1,j))
            glmc3 = G * im.getpixel((i,j)) + im.getpixel((i-1,j-1))
            hist[glmc0] = hist[glmc0] + 1
            hist[glmc1] = hist[glmc1] + 1
            hist[glmc2] = hist[glmc2] + 1
            hist[glmc3] = hist[glmc3] + 1
            j+=1
        i+=1
        
    plt.plot(hist)
    plt.show
    return hist

ruta = "baboon.jpg"
im = Image.open(ruta)
glcm(im)