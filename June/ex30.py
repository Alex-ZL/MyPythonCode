#!/usr/bin/python
##exercise 30
people = 50
cars = 40
buses = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if buses > cars:
	print "That's too many bused."
elif buses < cars:
	print "Maybe we could take the bused."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
