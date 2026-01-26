from PIL import Image

def extraerCanales(im):
    CMYK=im.convert('CMYK')
    YCbCr=im.convert('YCbCr')

    c, m, y, k = CMYK.split()
    c.save("canal_C_CMYK.jpg")
    m.save("canal_M_CMYK.jpg")
    y.save("canal_Y_CMYK.jpg")
    k.save("canal_K_CMYK.jpg")
    
    # Extraer los canales de YCbCr
    y, cb, cr = YCbCr.split()
    y.save("canal_Y_YCbCr.jpg")
    cb.save("canal_Cb_YCbCr.jpg")
    cr.save("canal_Cr_YCbCr.jpg")

    



ruta = "baboon.jpg"
im = Image.open(ruta)
extraerCanales(im)
