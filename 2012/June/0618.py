#!/usr/bin/python

def m2i(meters):
	return (meters*39.37)

def k2p(kilogram):
	return (kilogram*2.2046)

my_name = 'Alex Zhang'
my_age = 24 
my_height = m2i(1.70) #meters converted into inches
my_weight = k2p(70) #kilograms converted into pounds
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "It's a little heavy, you need to more attention on this."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the drink." % my_teeth

print "If I add %d, %d and %d I get %.2f." %(
		my_age, my_height, my_weight, my_age+my_height+my_weight)
