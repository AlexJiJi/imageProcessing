from PIL import Image

def quitarazul(im):
    n,m = im.size
    azul = Image.new('RGBA', (n,m))
    i = 0
    r,g,b = im.getpixel((1,1))
    quitar = tuple([r,g,b])
    while i < n:
        j = 0
        while j < m:
            r, g, b = im.getpixel((i,j))
            actual = tuple([r,g,b])
            if actual == quitar:
                pixel = tuple([r,g,b,0])
            else:
                pixel = tuple([r,g,b,255])
            azul.putpixel((i,j), pixel)
            
            j +=1
        i += 1
    azul.save("sinazul.png")
    return azul


ruta = "manzana.jpg"
im = Image.open(ruta)
im = quitarazul(im)
im.show()