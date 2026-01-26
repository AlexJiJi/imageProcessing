from PIL import Image


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
            escala_gris.putpixel((i,j), gris)
            j+=1
        i+=1
    return escala_gris



def brilloX(im):
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
    return promedio

def umbral(im):
    br = brilloX(im)
    im = escala_grises(im)
    n = im.size[0]
    m = im.size[1]
    umbr = Image.new('L',(n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            pixel = im.getpixel((i,j))
            if (pixel >= br):
                pixel = 255
            else:
                pixel = 0
            umbr.putpixel((i,j),pixel)
            j+=1
        i+=1
        umbr.save("umbralxbrillo.jpg")
    return umbr
    

ruta = "manzana.jpg"
im = Image.open(ruta)
im = umbral(im)
im.show()
