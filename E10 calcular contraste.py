from PIL import Image
import math as np

def Calcular_brillo(im):
    n,m = im.size
    suma= 0
    i = 0
    while i < n:
        j = 0
        while j < m:
            r, g, b = im.getpixel((i,j))
            gris = (r+g+b)/3
            suma = suma + gris
            j +=1
        i += 1
    total = n * m
    promedio = suma / total
    promedio = round(promedio)
    return promedio

def calcular_contraste(im):
    n,m = im.size
    numpix = n * m
    brillo = Calcular_brillo(im)
    brillo = round(brillo)
    suma = 0
    print(f'brillo: {brillo}')
    i = 0
    while i < n:
        j = 0
        while j < m:
            r, g, b = im.getpixel((i,j))
            pixel = round((r+g+b)/3)
            suma = suma + pixel -brillo
            j +=1
        i += 1
    cglobal = suma * suma
    contraste = np.sqrt((cglobal)/numpix)
    contraste = round(contraste)
    print(f'Contraste: {str(contraste)}')
    
ruta = "Lichtenstein.jpg"
im = Image.open(ruta)
calcular_contraste(im)









