#!/usr/bin/python
#-*- coding:utf-8 -*-

"""Fibonacci iterator"""
class Fib:
	"""a interator for Fibonacci sequence"""
	def __init__(self, max):
		self.max = max

	def __iter__(self):
		self.a = 0
		self.b = 1
		return self

	def next(self):
		fib = self.a
		if fib > self.max:
			raise StopIteration
		self.a, self.b = self.b, self.a+self.b
		return fib


def Fib_gen(max):
	"""Generator function for Fibonacci sequence"""
	a, b = 0, 1
	while a < max:
		yield a
		a, b = b, a+b

def perm(items, n=None):
	"""Generate all array"""
	if n is None:
		n = len(items)
	for i in range(len(items)):
		v = items[i:i+1]
		if n==1:
			yield v
		else:
			rest = items[:i] + items[i+1:]
			for p in perm(rest,n-1):
				yield v+p

def comb(items,n=None):
	"""Generate all possible combination"""
	if n is None:
		n = len(items)
	for i in range(len(items)):
		v = items[i:i+1]
		if n==1:
			yield v
		else:
			rest = items[i+1:]
			for c in comb(rest, n-1):
				yield v+c

#print "Comb: " + str(list(comb("abc",2)))
#print "Perm: " + str(list(perm("abc",2)))

class TestIterator:
	value = 0
	def next(self):
		self.value +=1
		if self.value > 10: raise StopIteration
		return self.value
	def __iter__(self):
		return self

#ti = TestIterator()
#print list(ti)

def flatten(nested):
	for sublist in nested:
		for element in sublist:
			yield element

nested = [[1,2],[3,4],[5]]
for num in flatten(nested):
	print num
