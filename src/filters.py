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

    def median_filter(self, gray_array):
        """
        to reduce noise in image
        :param gray_array : takes array of gray image
        :returns : array with reduced noise
        """
        w, h = gray_array.shape[0], gray_array.shape[0]
        for i in range(w):
            for j in range(h):
                self.median(i, j, gray_array)
        misc.imsave('./img/filter_check.jpeg', gray_array)
        return gray_array

    def median(self, x, y, array):
        """
        find median of a particular location in 2D array
        :param x: row coordinate of location
        :param y: column of the location
        :param array: 2D array itself
        Assign Median of array to location
        and  returns None
        """
        window_size = 5
        if x == 0 or x == array.shape[0] - 1:
            window_size -= 1
        if y == 0 or y == array.shape[1] - 1:
            window_size -= 1
        window = [0] * window_size
        i = 0
        window[i] = array[x, y]
        i += 1
        if x != 0:
            window[i] = array[x-1, y]
            i += 1
        if y != 0:
            window[i] = array[x, y-1]
            i += 1
        if x != array.shape[0]-1:
            window[i] = array[x + 1, y]
            i += 1
        if y != array.shape[1] - 1:
            window[i] = array[x, y + 1]
        if window_size % 2 == 1:
            to_allot = self.quick_select(window, int(window_size/2))
        else:
            to_allot = (self.quick_select(window, int(window_size / 2)) +
                        self.quick_select(window, window_size / 2 - 1)) / 2
        array[x, y] = to_allot
        return

    def quick_select(self, array, k):
        """
        Perform quick select operation i.e find kth minimum element from array
        Time Complexity: O(n) for average case and O(n^2) for worst cases
        param a: Array on which operation would perfom
        param k: kth minimun element have to find
        return: returns kth minimum value
        """
        start = 0
        end = len(array) - 1
        is_found = False
        while not is_found:
            pos = self.partition(array, start, end)
            if pos == k:
                is_found = True
                return array[pos]
            elif pos < k:
                start = pos + 1
            else:
                end = pos - 1

    def partition(self, array, start, end):
        """
        Perform Partition Operation on array a.
        Time Complexity: O(nLogn)
        Auxiliary Space: O(n)
        :param a: Iterable of elements
        :param start: pivot value for array
        :param end: right limit of array
        :return: return i value for function, used in partitioning of array.
        """
        i = start - 1
        pivot = array[end]
        for j in range(start, end):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        i += 1
        array[i], array[end] = array[end], array[i]
        return i

    def otsu_binarization(self, gray_array):
        