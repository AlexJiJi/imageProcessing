from PIL import Image
import matplotlib.pyplot as plt

ruta = "baboon.jpg"
im = Image.open(ruta)
plt.figure()
plt.imshow(im)
im.show()