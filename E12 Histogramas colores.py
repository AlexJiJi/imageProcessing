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

def escala_r(im):
    n = im.size[0]
    m = im.size[1]
    escala_gris = Image.new('L',(n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            escala_gris.putpixel((i,j),r)
            j+=1
        i+=1
    return escala_gris

def escala_g(im):
    n = im.size[0]
    m = im.size[1]
    escala_gris = Image.new('L',(n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            escala_gris.putpixel((i,j),g)
            j+=1
        i+=1
    return escala_gris

def escala_b(im):
    n = im.size[0]
    m = im.size[1]
    escala_gris = Image.new('L',(n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            escala_gris.putpixel((i,j),b)
            j+=1
        i+=1
    return escala_gris

def histogramaRGB(im):
    imr = escala_r(im)
    ren, col = imr.size
    total = ren * col
    a = np.asarray(imr, dtype = np.float32)
    a = a.reshape(1, total)
    a = a.astype(int)
    a = max(a)
    grises = max(a)
    vec = np.zeros(grises + 1)
    for i in range(total-1):
        valor = a[i]
        vec[valor] = vec[valor] + 1
    plt.title("Canal Rojo")
    plt.plot(vec)
    plt.show()
    
    img = escala_g(im)
    ren, col = img.size
    total = ren * col
    a = np.asarray(img, dtype = np.float32)
    a = a.reshape(1, total)
    a = a.astype(int)
    a = max(a)
    grises = max(a)
    vec = np.zeros(grises + 1)
    for i in range(total-1):
        valor = a[i]
        vec[valor] = vec[valor] + 1
    plt.title("Canal Verde")
    plt.plot(vec)
    plt.show()
    
    imb = escala_b(im)
    ren, col = imb.size
    total = ren * col
    a = np.asarray(imb, dtype = np.float32)
    a = a.reshape(1, total)
    a = a.astype(int)
    a = max(a)
    grises = max(a)
    vec = np.zeros(grises + 1)
    for i in range(total-1):
        valor = a[i]
        vec[valor] = vec[valor] + 1
    plt.title("Canal Azul")
    plt.plot(vec)
    plt.show()
    
def histograma3x1(im):
    #colores = escala_grises(im)
    colores = im.split()
    
    histogram_fig = plt.figure("Histogramas")
    histogram_fig.subplots_adjust(hspace = 0.5, wspace = 0.5)
    
    i = 1
    for color in colores:
        ax = histogram_fig.add_subplot(2,2,i)
        ax.plot(color.histogram())
        i+=1
    plt.rcParams["figure.figsize"] = [12.8, 9.6]
    plt.show()
    
    
    
ruta = "baboon.jpg"
im = Image.open(ruta)
histograma3x1(im)



