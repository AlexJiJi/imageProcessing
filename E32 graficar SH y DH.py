from PIL import Image
from matplotlib import pyplot as plt


def escala_grises(im):
    n = im.size[0]
    m = im.size[1]
    escala_gris = Image.new('L',(n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r,g,b = im.getpixel((i,j))
            gris = (r+g+b)/3
            gris = round(gris)
            pixel = gris
            escala_gris.putpixel((i,j),pixel)
            j+=1
        i+=1
    return escala_gris

def SHDH(im):
    DH = []
    SH = []
    for _ in range(512):
        SH.append(0)
        DH.append(0)
        
    im = escala_grises(im)
    n,m = im.size
    i = 1
    G = 256
    while i < n - 1:
        j = i
        while j < m - 1:
            sh1 = im.getpixel((i,j)) + im.getpixel((i-1,j-1))
            SH[sh1] = SH[sh1] + 1
            sh1 = im.getpixel((i,j)) + im.getpixel((i-1,j))
            SH[sh1] = SH[sh1] + 1
            sh1 = im.getpixel((i,j)) + im.getpixel((i-1,j+1))
            SH[sh1] = SH[sh1] + 1
            sh1 = im.getpixel((i,j)) + im.getpixel((i,j-1))
            SH[sh1] = SH[sh1] + 1
            sh1 = im.getpixel((i,j)) + im.getpixel((i,j+1))
            SH[sh1] = SH[sh1] + 1
            sh1 = im.getpixel((i,j)) + im.getpixel((i+1,j-1))
            SH[sh1] = SH[sh1] + 1
            sh1 = im.getpixel((i,j)) + im.getpixel((i+1,j))
            SH[sh1] = SH[sh1] + 1
            sh1 = im.getpixel((i,j)) + im.getpixel((i+1,j+1))
            SH[sh1] = SH[sh1] + 1
            
            sh1 = im.getpixel((i,j)) - im.getpixel((i-1,j-1)) + G
            DH[sh1] = DH[sh1] + 1
            sh1 = im.getpixel((i,j)) - im.getpixel((i-1,j)) + G
            DH[sh1] = DH[sh1] + 1
            sh1 = im.getpixel((i,j)) - im.getpixel((i-1,j+1)) + G
            DH[sh1] = DH[sh1] + 1
            sh1 = im.getpixel((i,j)) - im.getpixel((i,j-1)) + G
            DH[sh1] = DH[sh1] + 1
            sh1 = im.getpixel((i,j)) - im.getpixel((i,j+1)) + G
            DH[sh1] = DH[sh1] + 1
            sh1 = im.getpixel((i,j)) - im.getpixel((i+1,j-1)) + G
            DH[sh1] = DH[sh1] + 1
            sh1 = im.getpixel((i,j)) - im.getpixel((i+1,j)) + G
            DH[sh1] = DH[sh1] + 1
            sh1 = im.getpixel((i,j)) - im.getpixel((i+1,j+1)) + G
            DH[sh1] = DH[sh1] + 1
            
            j+=1
        i+=1
        
    #plt.plot(SH, label ="SH")
    #plt.plot(DH, label ="DH")
    #plt.title("SH y DH")
    #plt.legend()
    #plt.show()
    
    plt.plot(SH)
    plt.title("SH")
    plt.show()
    
    plt.plot(DH)
    plt.title("DH")
    plt.show()
    



ruta = "Lichtenstein.jpg"
im = Image.open(ruta)
SHDH(im)