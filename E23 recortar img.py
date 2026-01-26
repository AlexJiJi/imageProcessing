from PIL import Image



def segmentar(im):
    n,m = im.size
    print(f'n= {n}\nm= {m}\n')
    print("Ingrese las coordenadas a cortar: ")
    x1 = int(input("X1: "))
    y1 = int(input("Y1: "))
    x2 = int(input("X2: "))
    y2 = int(input("Y2: "))
    
    #x1=10
    #y1=10
    #x2=200
    #y2=200
    
    segmento = im.crop((x1,y1,x2,y2))
    return segmento

ruta = "baboon.jpg"
im = Image.open(ruta)
im = segmentar(im)
im.show()
