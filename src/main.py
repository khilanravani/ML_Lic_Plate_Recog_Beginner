import numpy as np
import scipy as sc
from PIL import Image


def input():
    """
    Work:       input function opens the image from img folder
    Returns:    It returns variable contain image as
                well an 2D array which contain (R, G, B)
                value of cooardinate (x, y)
    """
    img = Image.open('./img/img_test2.jpeg')
    pix = img.load()
    return img, pix


def main():
    img, img_array = input()
    img.show()
    print img_array[0, 0]


if __name__ == '__main__':
    main()
