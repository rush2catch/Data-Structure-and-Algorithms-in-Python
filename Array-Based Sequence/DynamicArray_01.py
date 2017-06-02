# provides getsizeof() function
import sys

data = []
for k in range(20):
    a = len(data)               # number of elements
    b = sys.getsizeof(data)     # actual sizes in bytes
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    print(id(data))

    data.append(None)           # increase size by None
del data


