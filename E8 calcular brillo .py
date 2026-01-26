from PIL import Image


def brillo(im):
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
    print(f'El brillo total es {str(promedio)}')

    
ruta = "baboon.jpg"
im = Image.open(ruta)
im = brillo(im)
#im.show() 








