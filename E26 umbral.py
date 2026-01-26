from skimage import filters
from skimage.io import imread
from PIL import Image


def aplicar_umbral(im, umbr):
    n,m = im.shape
    otsu = Image.new('1', (m,n))
    i = 0
    while i < n:
        j = 0
        while j < m:
            pixel = im[i,j] * 255
            if pixel > umbr:
                pixel = 1
            else:
                pixel = 0
            otsu.putpixel((j,i), pixel)
            j +=1
        i += 1
        otsu.save("otsu.jpg")
    return otsu

im = imread("baboon.jpg", as_gray = True)
umbral = filters.threshold_otsu(im)
umbral = round(umbral * 255)
print(f'umbral: {umbral}')
im = aplicar_umbral(im, umbral)
im.show()