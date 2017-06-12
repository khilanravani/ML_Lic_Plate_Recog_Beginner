import sys
import numpy as np
import scipy as sp
from PIL import Image, ImageFilter as imf
from scipy import misc
img = Image.open("img_test2.jpeg")
print(img.format, img.size, img.mode)
rect = (50,50,100,100)
re = img.crop(rect)
#r.show()
r,g,b = img.split()
print r,g,b
k = Image.merge("RGB",(b, r, g))
#k.show()
#img.show()
img = Image.open("img_test2.jpeg")
#split the image into individual bands
source = img.split()

R, G, B = 0, 1, 2

# select regions where red is less than 100
mask = source[R].point(lambda i: i < 100 and 255)

# process the green band
out = source[G].point(lambda i: i * 0.7)

# paste the processed band back, but only where red was < 100
source[G].paste(out, None, mask)

# build a new multiband image
#mask.show()
mask.save('/home/heet/Git/ML_Lic_Plate_Recog_Beginner/Test/op.jpg')
print img.getpixel((2, 3))
pix = img.load()
print pix[0,0]
w,h = img.size
print w,h
for i in range(w):
	for j in range(h):
		sor = pix[i,j]
		p=[0,0,0]
		p[0] = abs(sor[0]-sor[1])
		p[1] = abs(sor[1]-sor[2])
		p[2] = abs(sor[2]-sor[0])
		pix[i,j] = tuple(p)
img.show()
img.save('/home/heet/Git/ML_Lic_Plate_Recog_Beginner/Test/op2.jpg')