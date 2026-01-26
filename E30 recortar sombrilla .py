from PIL import Image


def quitar_amarillo(im):
    n,m = im.size
    paraguas = Image.new('RGBA', (n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r, g, b = im.getpixel((i,j))
            if b > r and b > g:
                gris = round((r + g + b)/3)
                pixel = tuple([gris, gris, gris,0])
                paraguas.putpixel((i,j), pixel)
            else:
                pixel = tuple([r,g,b, 255])
                paraguas.putpixel((i,j), pixel)
                
            j +=1
        i += 1
    paraguas.save("Sombrilla_recortada.png")
    return paraguas


ruta = "sombrilla.jpg"
im = Image.open(ruta)
im = quitar_amarillo(im)
im.show()

