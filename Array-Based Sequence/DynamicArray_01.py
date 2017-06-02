# provides getsizeof() function
import sys

data = []
for k in range(20):
    a = len(data)               # number of elements
    b = sys.getsizeof(data)     # actual sizes in bytes
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.append(None)           # increase size by None


for i in range(21):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, b))
    data.pop()

