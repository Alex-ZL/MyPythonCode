#!/usr/bin/python
## exercise 43
from sys import exit
from random import randint

class Game(object):

	def __init__(self, start):
		self.quips = [
				"You died. You kinda suck at this.",
				"Your mom would be proud. If she were smarter.",
				"Such a luser.",
				"I have a small puppy that's better at this."
			]
		self.start = start

	def play(self):
		next_room_name = self.start

		while 1:
			print "\n--------------"
			room = getattr(self, next_room_name)
			next_room_name = room()

	def death(self):
		print self.quips[randint(0, len(self.quips)-1)]
		exit(1)

	def central_corridor(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destoryed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission is to ge the neutron destruct bomb from the Weapons Armory,"
		print "put is in the bridge, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the "
		print "Armory and about to pull a weapon to blast you."

		action = raw_input("> ")

		if action == "shoot!":
			print "Quick on the draw you yank out your blaster and fire it at the Gothon."
			print "His clown costume is flowing and moving around his body, which throws"
			print "off your aim. Your laser hits his costume but misses him entirely. This"
			print "makes him fly into an insane rage and blast you repeatedly in the face until"
			print "you are dead. Then he eats you."
			return 'death'

		elif action == "dodge!":
			print "Like a world class boxer you dodge, weave, slip and slide right"
			print "as the Gothon's blaster cranks a laser past your head."
			print "In the middle of your artful dodge yours foot slips and you"
			print "bang your head on the metal wall and pass out."
			print "You wake up shortly after only to die as the Gothon stomps on"
			print "your head and eats you."
			return 'death'

		elif action == "tell a joke":
			print "Lucky for you they made you learn Gothon insults in the academy."
			print " You tell the one Gothon joke you know:"
			print "Lbhe zbgure vf fb sng, jura fur fvgf nebhag gur ubhfr, fur fvgf nebhag gur ubhfr."
			print "The Gothon stops, tries not to laugh, then busts out laughing and can't move."
			print "While he's laughin COMUPg you run up and shoot him square in the head"
			print "putting him   ijdown, then jump through the Weapon Armory door."
			return 'last_weapon_armory'

		else
			print "DOES NOT COMPUTE!"
			return 'central_corridor'

	def last_ weapon_armory(self):
		print "You do a dive roll into the Weapon Armory, crouch and scan the room"
		print "wrofor more Gothons that might be hiding It's dead quiet, too quiet."
		print "wwYou stand up and run to the far side of the room and find the"
		print "neutron bomb in its container. There's a keypad lock on the box"
		print "and you need the code to get the bomb out. If you get the code"
		print " wrong 10 times then the lock closes forever and you can't"
		print "get the bomb. The code is 3 digits."
		code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		gesses = 0

		while guess != code and guesses < 10:
			print "BZZZZEDDD!"
			guesses += 1
			guess = raw_input("[keypad]> ")

		if guess == code:
			print "The container clicks open and the seal breaks, letting gas out."
			print " You grab the neutron bomb and run as fast as you can to the "
			print "bridge where you must place it in the right spot."
			return 'the_bridge'
		else:
			print "The lock buzzes one last time and then you hear a sickening"
			print "melting sound as the mechanism is fused together."
			print "You decide to sit there, and finally the Gothons blow up the"
			print "ship from their ship and you die."
			return 'death'


