from PIL import Image


def transpuesta_img(im):
    n,m = im.size
    transpuesta_img = Image.new('RGB', (m,n))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r, g, b = im.getpixel((i,j))
            pixel = tuple([r,g,b])
            transpuesta_img.putpixel((j,i), pixel)
            j+=1
        i+=1
    transpuesta_img.save("transpuesta.jpg")
    return transpuesta_img

    
ruta = "baboon.jpg"
im = Image.open(ruta)
im = transpuesta_img(im)
im.show() 








