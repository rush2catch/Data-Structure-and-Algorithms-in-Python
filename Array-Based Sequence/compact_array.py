import sys
from array import array

compact_primes = array('i', [2, 3, 5, 7, 11, 13])
print(id(compact_primes))
print(len(compact_primes))
print(sys.getsizeof(compact_primes))
for i in range(len(compact_primes)):
    print(compact_primes[i], id(compact_primes[i]))

refer_primes = [2, 3, 5, 7, 11, 13]
print(id(refer_primes))
print(len(refer_primes))
print(sys.getsizeof(refer_primes))
for i in range(len(refer_primes)):
    print(refer_primes[i], id(refer_primes[i]))