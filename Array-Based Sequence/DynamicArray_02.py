# provide low-level arrays
import ctypes

"""
A dynamic array class akin to a simplified Python List[] class.
"""
class DynamicArray(object):

    # creating an empty array.
    def __init__(self):
        self._n = 0                                         # count actual elements
        self._capacity = 1                                  # default array capacity
        self._A = self._make_array(self._capacity)          # low-level array

    # return numbers of elements stored in the array
    def __len__(self):
        return self._n

    # return element at index k
    def __getitem__(self, k):
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    # add object to the end of the array:
    def append(self, item):
        # when the room is not enough, double the capacity
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = item
        self._n += 1

    # resize internal array to capacity c
    def _resize(self, c):
        B = self._make_array(c)                             # new bigger array
        for k in range(self._n):                            # for each existing value
            B[k] = self._A[k]
        self._A = B                                         # use the bigger array
        self._capacity = c

    # return new array with capacity c
    def _make_array(self, c):
        return (c * ctypes.py_object())
