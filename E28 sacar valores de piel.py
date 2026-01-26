from PIL import Image


def sacar_piel(im):
    n,m = im.size
    piel = Image.new('RGB', (n,m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r, g, b = im.getpixel((i,j))
            gris = round((r + g + b)/3)
            mayor = max(r, g, b)
            menor = min(r, g, b)
            if (((r > 76) and (r < 240)) and ((g > 14) and (g < 221)) and ((b > 45) and (b < 207)) and ((mayor - menor) > 15) and ((abs(r - g) > 17) and (abs(r - g) < 81)) and ((abs(r - b) > 32) and (abs(r - b) < 114)) and ((abs(g - b) > 4) and (abs( g - b) < 37))):
                if r > g and g > b:
                    pixel = tuple([r,g,b])
                    piel.putpixel((i,j), pixel)
                else:
                    pixel = tuple([gris,gris,gris])
                    piel.putpixel((i,j), pixel)
            else:
                pixel = tuple([gris,gris,gris])
                piel.putpixel((i,j), pixel)
                
            j +=1
        i += 1
    return piel


ruta = "barbara.jpg"
im = Image.open(ruta)
im = sacar_piel(im)
im.show()