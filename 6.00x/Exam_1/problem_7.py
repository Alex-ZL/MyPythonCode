# coding: utf-8
def McNuggets(n):
    if n == 0:
        return False
    count = n/6+1
    for c in xrange(count):
        for b in xrange(count):
             for a in xrange(count):
                 if a*6+b*9+c*20 == n:
                     return True
    return False

print McNuggets(6)
print McNuggets(9)
print McNuggets(15)
print McNuggets(0)
