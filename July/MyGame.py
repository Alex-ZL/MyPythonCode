#!/usr/bin/python
## A simple game about magic and sword, enjoy it!
from random import randint
import sys

class game(object):
	def __init__(self):
		pass

	def weapon(self, role):
		"""choose right weapon for the role according to his property"""
		pass
	pass

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

		if self.career = "Warrior":
			self.hp = 120
		elif self.career = "Archer":
			self.hp = 100
		else:
			self.hp = 90
	
	def attack(self):
		if 

	pass

class monster(object):
	pass
