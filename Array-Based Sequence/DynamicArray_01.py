# provides getsizeof() function
import sys

data = []
for k in range(50):
    a = len(data)               # number of elements
    b = sys.getsizeof(data)     # actual sizes in bytes
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, (b-64)//8))
    data.append(None)           # increase size by None

print('-' * 100)
for i in range(50):
    a = len(data)
    b = sys.getsizeof(data)
    print("Length: {0:3d}; Size in bytes: {1:4d}".format(a, (b-64)//8))
    data.pop()

