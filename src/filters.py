from PIL import Image
import numpy as np
from scipy import misc


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
