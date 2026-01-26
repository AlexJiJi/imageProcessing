from PIL import Image


def min_imagen(im):
    n,m = im.size
    minimo_imagen = Image.new('L',(n,m))
    valormin = 255
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            minpix = min(r,g,b)
            if minpix < valormin:
                valormin = minpix
            minimo_imagen.putpixel((i,j), minpix)
            j += 1
        i+=1
    minimo_imagen.save("minimo.jpg")
    print(f'El valor minimo es: {str(valormin)}')
    return minimo_imagen
    
ruta = "baboon.jpg"
im = Image.open(ruta)
im = min_imagen(im)
im.show() 








