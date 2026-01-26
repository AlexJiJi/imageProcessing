from PIL import Image


ruta = "baboon.jpg"
im = Image.open(ruta)


r,g,b = im.getpixel((100,100))
ima = Image.new('RGBA',(100,100))

for i in range(99):
    for j in range(99):
        pixel = tuple([r,g,b])
        ima.putpixel((i,j),pixel)

ima.show() # muestra el pixel seleccionado

R = r/255
G = g/255
B = b/255

K = 1 - max(R,G,B)

C = ((1-R-K)/(1-K))
M = ((1-G-K)/(1-K))
Y = ((1-G-K)/(1-K))

print(f'C: {C} \nM: {M} \nY: {Y}')