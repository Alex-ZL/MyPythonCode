#!/usr/bin/python

class entryExit(object):
	def __init__(self, f):
		self.f=f

	def __call__(self):
		print "Entering", self.f.__name__
		self.f()
		print "Exited", self.f.__name__

def f_entryExit(f):
	def new_f():
		print "f_entering", f.__name__
		f()
		print "f_exited",f.__name__
	return new_f

@f_entryExit
def func1():
	print "inside func1()"

@f_entryExit
def func2():
	print "inside func2()"

class decoratorWithoutArguments(object):
	def __init__(self,f):
		"""
		If there are no decorator arguments, the funcion
		to be decorated is passed to the constructor.
		"""
		print "Inside __init__()"
		self.f=f

	def __call__(self, *args):
		"""
		The __call__ method is not called until the
		decorated function is called.
		"""
		print "Inside __call__()"
		self.f(*args)
		print "After self.f(*args)"

class decoratorWithArguments(object):
	def __init__(self, arg1, arg2, arg3):
		"""
		If there are decorator arguments, the function
		to be decorated is not passed to the constructor!
		"""

		print "Inside __init__()"
		self.arg1 = arg1
		self.arg2 = arg2
		self.arg3 = arg3

	def __call__(self, f):
		"""
		If there are decorator arguments, __call__() is only called
		once, as part of the decoration process! You can only give
		it a single argument, which is the function object.
		"""
		print "Inside __call__()"
		def wrapped_f(*args):
			print "Inside wrapped_f()"
			print "Decorator arguments:", self.arg1, self.arg2, self.arg3
			f(*args)
			print "After f(*args)"
		return wrapped_f

def decoratorFunctionWithArguments(arg1, arg2, arg3):
	def wrap(f):
		print "Inside wrap()"
		def wrapped_f(*args):
			print "Inside wrapped_f()"
			print "Decorator arguments:", arg1, arg2, arg3
			f(*args)
			print "After f(*args)"
		return wrapped_f
	return wrap

@decoratorFunctionWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
	print "sayHello arguments:", a1, a2, a3, a4

print "After decoration"

print "Preparing to call sayHello()"
sayHello("say", "hello", "arguments", "list")
print "after first sayHello() call"
sayHello("a", "different", "set of", "arguments")
print "after second sayHello() call"
