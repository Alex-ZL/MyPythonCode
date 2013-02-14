#!/usr/bin/python
def foo():
	a = 1
	def bar():
		a = 2
		print a, id(a)

	bar()
	print a, id(a)
	
foo()

flist = []

for i in xrange(3):
	def func(x): return x*i
	flist.append(func)

for f in flist:
	print f(100)
