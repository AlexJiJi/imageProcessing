#COnver rgba a rgb
from PIL import Image

ruta = "imaTransparente.png"
im = Image.open(ruta)

def remover_transparencia(im, color_fondo=(255, 255, 255)):

    if im.mode != 'RGBA':
        im = im.convert('RGBA')
    
   
    fondo = Image.new('RGBA', im.size, color_fondo + (255,))  

    # Combinar la imagen con el fondo
    imagen_sin_transparencia = Image.alpha_composite(fondo, im)


    imagen_sin_transparencia = imagen_sin_transparencia.convert('RGB')
    
    imagen_sin_transparencia.save("imagen_sin_transparencia.png")
    return imagen_sin_transparencia


im = remover_transparencia(im)
im.show()
