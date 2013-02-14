#!/usr/bin/python

def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, agr2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
	print "arg1: %r, agr2: %r" % (arg1, arg2)

def print_one(arg1):
	print "arg1: %r" % arg1

def print_none():
	print "Nothing!"

print_two("Emma","He")
print_two_again("My","girl")
print_one("only")
print_none()

def checklist():
	print """
	1. Did you start your function definition with def?
	2. Does your function name have only characters and _(underscore) characters?
	3. Did you put an open parenthesis ( right after the function name?
	4. Did you put your arguments after the parenthesis (separated by commas?
	5. Did you make each argument unique (meaning no duplicated names).
	6. Did you put a close parenthesis and a colon ): after the arguments?
	7. Did you indent all lines of code you want in the function 4 spaces? No more, no less.
	8. Did you "end" your function by going back to writing with no indent(dedenting we call it)?

	And when you run(aka "use" or "call") a function, check these things:
	1. Did you call/use/run this function by typing its name?
	2. Did you put ( character after the name to run it?
	3. Did you put the values you want into the parenthesis separated by commas?
	4. Did you end the function call with a ) character.
	"""
checklist()
