from PIL import Image


def bgr(im):
    n,m = im.size
    new = Image.new('RGB', (n, m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r, g, b = im.getpixel((i, j))
            pixel = tuple([b,g,r])
            new.putpixel((i,j),pixel) 
            j += 1
        i += 1
    new.save("bgr.jpg")
      
    return new

ruta = "baboon.jpg"
im = Image.open(ruta)
im = bgr(im)
im.show()