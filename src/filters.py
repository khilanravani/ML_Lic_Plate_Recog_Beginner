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
        # misc.imsave('./img/gray_check.jpg', gray)
        return gray

    def histogram_equalisation(self, gray_array):
        """
        hitogram equalisation method enhance contrast of image
        :param gray_array: array of gray scale image
        :Returns : It returns enhanced array
        for more go to https://en.wikipedia.org/wiki/Histogram_equalization
        """
        freq = [0] * 256
        wt, ht = gray_array.shape[0], gray_array.shape[1]
        total = wt * ht - 1
        min_pos = -1
        for i in range(wt):
            for j in range(ht):
                freq[int(gray_array[i, j])] += 1
                if min_pos == -1 or gray_array[i, j] < min_pos:
                    min_pos = int(gray_array[i, j])
        cfeq = [0] * 256
        cfeq[0] = freq[0]
        for i in range(1, 256):
            cfeq[i] = cfeq[i - 1] + freq[i]
        h = [0] * 256
        for v in range(256):
            h[v] = (((cfeq[v] - cfeq[min_pos]) * 1.0) / total) * 255
        for i in range(wt):
            for j in range(ht):
                gray_array[i, j] = h[int(gray_array[i, j])]
        return gray_array
