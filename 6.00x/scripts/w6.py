# coding: utf-8
def isPrime(n):
    if not isinstance(n,int):
        raise TypeError
    if n <= 0:
        raise ValueError
    if n == 1:
        return True
    for i in xrange(2,int(n**0.5+1)):
        if i < n and n%i==0:
            return False
    return True
print isPrime(2)
print isPrime(6)
print isPrime(5)
