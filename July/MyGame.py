#!/usr/bin/python
## A simple game about magic and sword, enjoy it!
from random import randint
import sys

class game(object):

#	def __init__(self):
#		initRole()


	def __init__(self):
		"""create a role with properties including career, weapon"""
		print "Welcome the world of sword and magic!"
		print "As a chosen one, you have to begin your advanture now"
		print "Willing or not, you must do something, so......"
		print "\n"
		print "MAKE YOUR CHOICE!!!!!!"
		print "First, you will have a test to decide your career."
		marks = 0
		try:
			marks += int(raw_input("Which way would you prefer in a fight? \n 1: melee combat. 2:hit and run. 1 or 2?"))
		except ValueError: 
			print "error input, please enter number!"
		properties = {"strength":10,
					  "agility":10,
					  "willpower":10,
					  "career":"Warrior",
					  "weapon":"sword",
					  }
		self.myrole = role(properties)
		print "Now you are a warrior!"

	def play(self):
		next_mission_name = 'valley'
		while 1:
			print "\n*********************"
			mission = getattr(self,next_mission_name)
			next_mission_name = mission(self.myrole)

	def valley(self, role):
		print "Here is valley, a gaint's manor"
		print role.attack()
		return 'jungle'

	def jungle(self, role):
		print "In the dark jungle, there lives a evil wizard"
		return 'castle'

	def castle(self, role):
		print "Lo and behold, you get to the dragon's castle"
		return 'death'

	def death(self, role):
		quips = [
			"Now or never, sorry you failed!",
			"It's not always the hero win the game",
			"Do you really try your best?",
			"Whatever, try again, you may win next time."
		]
		print quips[randint(0, len(quips)-1)]
		print "You could be a great " + role.career
		exit(1)
	


class role(object):
	"""basic role with properties and actions"""

	def __init__(self,properties):
		""" set the role's basic properties """
		
		self.strength = properties["strength"]
		self.agility = properties["agility"]
		self.willpower = properties["willpower"]
		self.luck = randint(1,10)
		self.career = properties["career"]
		self.weapon = properties["weapon"]

		if self.career == "Warrior":
			self.hp = 120
		elif self.career == "Archer":
			self.hp = 100
		else:
			self.hp = 90
	

	def attack(self):
		"""attack method return damage value depending on career"""

		if self.career == "Warrior":
			damage = 1.5*self.strength + 1*self.agility + 0.5*self.willpower + randint(0, self.luck)
		elif self.career == "Archer":
			damage = 1.2*self.strength + 1.4*self.agility + 0.4*self.willpower + randint(0, self.luck)
		else:
			damage = 0.4*self.strength + 0.9*self.agility + 1.7*self.willpower + randint(0, self.luck)

		if randint(0, self.agility) == 0:
			damage = 0
		return damage


MyGame = game()
MyGame.play()
