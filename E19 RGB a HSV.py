from PIL import Image



def hsv(im):
    n,m = im.size
    new = Image.new('RGB', (n, m))
    i = 0
    while i < n:
        j = 0
        while j < m:
            r, g, b = im.getpixel((i, j))
            R = r/255
            G = g/255
            B = b/255
            minimo = min(R, G, B)
            maximo = max(R, G, B)
            diferencia = maximo - minimo
            #print(diferencia)
            if diferencia == maximo:
                H = 0
            elif diferencia == minimo:
                H = 100
            elif diferencia != 0:  # Verificación para evitar división entre 0
                if maximo == R and G >= B:
                    H = (60 * ((G - B) / diferencia)) % 360
                elif maximo == R and G < B:
                    H = (60 * ((G - B) / diferencia) + 360) % 360
                elif maximo == G:
                    H = (60 * ((B - R) / diferencia) + 120) % 360
                elif maximo == B:
                    H = (60 * ((R - G) / diferencia) + 240) % 360
                    
            if maximo == 0:
                S = 0
            else:
                S = (diferencia/maximo)*100
            V = round(maximo)
            H = round(H)
            S = round(S)
            
            pixel = tuple([H,S,V])
            #print(f'H: {H}\nS: {S}\nV: {V}')
            new.putpixel((i,j), pixel)
            j += 1
        i += 1
        
    return new

ruta = "baboon.jpg"
im = Image.open(ruta)
im = hsv(im)
im.show()
