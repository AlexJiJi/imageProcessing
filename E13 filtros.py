from PIL import Image, ImageFilter

im = Image.open("baboon.jpg")
im_contorno = im.filter(ImageFilter.CONTOUR())
im_contorno.show()

im_blur = im.filter(ImageFilter.BLUR())
im_blur.show()

im_detail = im.filter(ImageFilter.DETAIL())
im_detail.show()

im_edge_enchance = im.filter(ImageFilter.EDGE_ENHANCE())
im_edge_enchance.show()

im_edge_enchance_more = im.filter(ImageFilter.EDGE_ENHANCE_MORE())
im_edge_enchance_more.show()

im_emboss = im.filter(ImageFilter.EMBOSS())
im_emboss.show()

find_edges = im.filter(ImageFilter.FIND_EDGES())
find_edges.show()

im_sharpen = im.filter(ImageFilter.SHARPEN())
im_sharpen.show()

im_smooth = im.filter(ImageFilter.SMOOTH())
im_smooth.show()

im_smoothmore = im.filter(ImageFilter.SMOOTH_MORE())
im_smoothmore.show()
