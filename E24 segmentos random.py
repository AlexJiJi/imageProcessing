from PIL import Image
import random



def segmentar(im):
    n, m =im.size
    
    i = 0
    mitadN=round(n/2)
    mitadM=round(m/2)
    while i<10:
        
        x1 = random.randrange(0,mitadN)
        y1 = random.randrange(0,mitadM)
        
        segmento = im.crop((x1,y1,x1+mitadN,y1+mitadM))
        #segmento.show()
        segmento.save("segmento"+str(i)+".jpg")
        i+=1


ruta = "baboon.jpg"
im = Image.open(ruta)
im = segmentar(im)

