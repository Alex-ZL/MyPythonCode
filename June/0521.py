#!/usr/bin/python

class Reverse:
	"""Iterator for looping over a sequence backwards"""
	def __init__(self,data):
		self.data = data
		self.index = len(data)
	def __iter__(self):
		return self
	def next(self):
		if self.index == 0:
			raise StopIteration
		self.index = self.index - 1
		return self.data[self.index]

def reverse(data):
	for index in range(len(data)-1,-1,-1):
		yield data[index]

for char in Reverse("keep moving, don't settle"):
	print char

for char in reverse("Always love you!"):
	print char
#First of all, we have to survive.

##First of all, we have to survive.
##After that,
##then, we need to feel more comfortable.
##
##first of all, we have to survive.
##first of all, we have to survive.
##first of all, we have to survive.
##first of all, we have to survive.
##first of all, we have to survive.
survive
