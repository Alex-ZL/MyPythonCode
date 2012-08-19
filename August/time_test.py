#!usr/bin/env python
## show run time of map
a = []
for i in range(1000000):
	a.append(i)

import time

start = time.time()
for i in range(10):
	b = sorted(a)
end = time.time()
t01 = end - start
print 'time 1:', t01

start = time.time()
for i in range(10):
	x = max(a) == min(a)
end = time.time()
t02 = end - start
print 'time 2:', t02

start = time.time()
for i in range(10):
	b = a[0]
x = all(map(lambda x:x == b, a))
end = time.time()
t03 = end -start
print 'time 3:', t03
