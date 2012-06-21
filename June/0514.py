#!/usr/bin/python
import exceptions
try:
	x = input("Enter the 1st num: ")
	y = input("Enter the 2nd num: ")
	print x/y
except(ZeroDivisionError,TypeError),e:
	print e
