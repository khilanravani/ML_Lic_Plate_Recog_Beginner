import numpy as np
import scipy as sc
from scipy import misc
from PIL import Image
from filters import filters


def input():
    """
    Work:       input function opens the image from img folder
    Returns:    It returns variable contain image as
                well an 2D array which contain (R, G, B)
                value of cooardinate (x, y)
        """
    pix = misc.imread('./img/img_test14.jpeg')
    return pix


def main():

    img_array = input()
    fliter_use = filters(img_array)
    gray_array = fliter_use.grayscale()
    gray_array = fliter_use.median_filter(gray_array)
    # remove below hash to check gray conversion of input image
    misc.imsave('./img/gray_tst.jpeg', gray_array)
    histo_array = fliter_use.histogram_equalisation(gray_array)
    # remove below hash to chack histogram conversion of image
    misc.imsave('./img/histo_test.jpeg', histo_array)
    # remove below hash to see grayscale array
    # print gray_array[4]

if __name__ == '__main__':
    main()
