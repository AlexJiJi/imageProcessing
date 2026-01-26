from PIL import Image




def efecto3d(im):
    n, m = im.size
    new = Image.new('RGB', (n, m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            if (i+10)>=n:
                r, g, b = im.getpixel((i, j))
                _, g5, _ = im.getpixel((i+10-n, j))
            else:
                r, g, b = im.getpixel((i, j))
                _, g5, _ = im.getpixel((i+10,j))
            pixel = tuple([r,g5,b,])
            new.putpixel((i,j), pixel)
            j += 1
        i += 1
    new.save("Efecto3d.jpg")
      
    return new

ruta = "baboon.jpg"
im = Image.open(ruta)
im = efecto3d(im)
im.show()
