from PIL import Image

def max_imagen(im):
    n,m = im.size
    maximo_imagen = Image.new('L',(n,m))
    valormax = 0
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            maxpix = max(r,g,b)
            if maxpix > valormax:
                valormax = maxpix
            maximo_imagen.putpixel((i,j), maxpix)
            j += 1
        i+=1
    maximo_imagen.save("maximo.jpg")
    print(f'El valor maximo es: {str(valormax)}')
    return maximo_imagen
    
ruta = "baboon.jpg"
im = Image.open(ruta)
im = max_imagen(im)
im.show() 








