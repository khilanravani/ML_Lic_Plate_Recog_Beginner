import Image
import sys
import numpy as np
import scipy as sp
from PIL import Image
from scipy import misc
img = Image.open("img_test2.jpeg")
f = misc.face(gray = True)
#misc.imsave('img_test2.jpeg',f)
#f = misc.imread('img_test2.jpeg')
#for i in range(246):
#	f[i] = i-1	
#j = Image.fromarray(f)
#j.save("/home/heet/Git/ML_Lic_Plate_Recog_Beginner/Test/gray2.jpg")
#print f
print img
