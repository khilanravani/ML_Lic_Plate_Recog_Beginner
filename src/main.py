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
    pix = misc.imread('./img/img_test2.jpeg')
    return pix


def main():

    img_array = input()
    fliter_use = filters(img_array)
    gray_array = fliter_use.grayscale()
    # remove below hash to see grayscale array
    # print gray_array


if __name__ == '__main__':
    main()
