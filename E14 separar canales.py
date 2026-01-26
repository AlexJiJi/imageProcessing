from PIL import Image

def DividirEn3Canales(im):
    n = im.size[0]
    m = im.size[1]
    escalaR = Image.new('L',(n,m))
    escalaG = Image.new('L',(n,m))
    escalaB = Image.new('L',(n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            escalaR.putpixel((i,j),r)
            escalaG.putpixel((i,j),g)
            escalaB.putpixel((i,j),b)
            j+=1
        i+=1
    escalaR.save("CanalR.jpg")
    escalaR.show()
    escalaG.save("CanalG.jpg")
    escalaG.show()
    escalaB.save("CanalB.jpg")
    escalaB.show()

ruta = "baboon.jpg"
im = Image.open(ruta)
im = DividirEn3Canales(im)
#im.show()