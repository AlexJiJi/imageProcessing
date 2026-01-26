from PIL import Image

def aplicar_transparencia(im):
    n = im.size[0]
    m = im.size[1]
    ima = Image.new('RGBA',(n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            pixel = tuple([r,g,b,28])
            ima.putpixel((i,j),pixel)
            j+=1
        i+=1
    ima.save("imaTransparente.png")
    return ima


ruta = "barbara.jpg"
im = Image.open(ruta)
im = aplicar_transparencia(im)
im.show()