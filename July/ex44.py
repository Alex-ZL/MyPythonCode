#!/usr/bin/python
## exercise 44
class parent(object):

	def implicit(self):
		print "parent implicit()"

	def override(self):
		print "parent override()"

	def altered(self):
		print "parent altered()"

class child(parent):

	def override(self):
		print "child override()"

	def altered(self):
		print "child, before parent altered()"
		super(child,self).altered()
		print "child, after parent altered()"

dad = parent()
son = child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()

class SuperFun(child, badstuff):
	pass

