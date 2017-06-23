from PIL import Image
import numpy as np
from scipy import misc
import math


class filters(object):

    def __init__(self, pix):
        self.pix = pix

    def grayscale(self):
        """
        Method covert RGB array to grayscale array
        returns grayscale array
        """
        w, h = self.pix.shape[0], self.pix.shape[1]
        gray = np.zeros((self.pix.shape[0], self.pix.shape[1]))
        for i in range(w):
            for j in range(h):
                color = self.pix[i, j]
                gray[i][j] = int(0.299*color[0] + 0.587*color[1]
                                 + 0.114*color[2])
        # remove below hash to check if output of image
        # misc.imsave('./img/op4.jpg', gray)
        return gray


    def histogram_equalisation(self, gray_array):
        freq = [0] * 8
        w, h =  gray_array.shape[0], gray_array.shape[1]
        total = w * h
        for i in range(w):
            for j in range(h):
                if gray_array[i, j] == 0.0:
                    index = 0
                else:
                    index = int(math.floor(math.log(gray_array[i, j], 2)))
                freq[index] += 1
        print freq
        cfeq = [0]*8
        cfeq[0] = (freq[0]*1.0) / total
        for i in range(1, 8):
            cfeq[i] = cfeq[i - 1] + ((freq[i]*1.0) / total)
        print cfeq
        for i in range(8):  
            cfeq[i] *= 7
        for i in range(w):
            for j in range(h):
                if gray_array[i, j] == 0.0:
                    index = 0
                else:
                    index = int(math.floor(math.log(gray_array[i, j], 2)))
                gray_array[i, j] = int(cfeq[index] ** 2)
        print cfeq
        return gray_array
