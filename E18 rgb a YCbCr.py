from PIL import Image

ruta = "baboon.jpg"
im = Image.open(ruta)

def YCbCr(im):
    n = im.size[0]
    m = im.size[1]
    new = Image.new('YCbCr',(n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            y = round((0.299 * r) + (0.587 * g) + (0.114 * b))
            Cr = round(128 + (0.5 * r) - (0.418688 * g) - (0.081312 * b))
            Cb = round(128 + (-0.168736 * r) - (0.331264 * g) + (0.5 * b))
            pixel = tuple([y,Cb,Cr])
            new.putpixel((i, j), pixel)
            j+=1
        i+=1    
        #print(f'y: {y}\nCr: {Cr} \nCb: {Cb}')
        new.save("YCrCb.jpg")

    return new


im = YCbCr(im)
im.show()
