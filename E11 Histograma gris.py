from PIL import Image
from matplotlib import pyplot as plt
import numpy as np


def escala_grises(im):
    n = im.size[0]
    m = im.size[1]
    modelo = im.mode
    escala_gris = Image.new('L',(n,m)) #Image.new(modelo,(n,m))  
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            gris = (r+g+b)/3
            gris = round(gris)
            pixel = gris #tuple([gris,gris,gris])
            escala_gris.putpixel((i,j),pixel)
            j+=1
        i+=1
    return escala_gris

def histograma(im):
    im = escala_grises(im)
    ren, col = im.size
    total = ren * col
    a = np.asarray(im, dtype = np.float32)
    a = a.reshape(1, total)
    a = a.astype(int)
    a = max(a)
    grises = max(a)
    vec = np.zeros(grises + 1)
    for i in range(total-1):
        valor = a[i]
        vec[valor] = vec[valor] + 1
    plt.plot(vec)
    plt.show()
    
ruta = "baboon.jpg"
im = Image.open(ruta)
histograma(im)
    
    
    
