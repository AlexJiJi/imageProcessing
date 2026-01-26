from PIL import Image

def calcular_brillo(im):
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
    return promedio

def agregar_brillo(im, aumento):
    n,m = im.size
    brillo = calcular_brillo(im)
    brillante = Image.new('RGB', (n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r, g, b = im.getpixel((i,j))
            if r > brillo:
                r += aumento
                if r > 255:
                    r = 255
            if g > brillo:
                g += aumento
                if g > 255:
                    g = 255
            if b > brillo:
                b += aumento
                if b > 255:
                    b = 255
            pixel = tuple([r,g,b])
            brillante.putpixel((i,j), pixel)
            j +=1
        i += 1
        brillante.save("brillante.jpg")
    return brillante
    
ruta = "baboon.jpg"
im = Image.open(ruta)
brillo = -1
while brillo < 1 or brillo > 255:
    brillo = int(input("Cuanto brillo quiere agregar?: "))

im = agregar_brillo(im, brillo)
im.show()









