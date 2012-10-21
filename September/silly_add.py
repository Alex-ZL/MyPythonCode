x = 1
y = 2
z = x + y
for i in xrange(100):
	x, y = y, x+y
	print x
