#!/usr/bin/python
## A simple game about magic and sword, enjoy it!
from random import randint
import sys

class game(object):

	def __init__(self):
		"""create a role with properties including career, weapon"""
		print "Welcome the world of sword and magic!"
		print "As a chosen one, you have to begin your advanture now"
		print "Willing or not, you must do something, so......"
		print "\n"
		print "MAKE YOUR CHOICE!!!!!!"
		print "First, you will have a test to decide your career."
		raw_input("Let's begin the test!")
		properties = {"strength":10,
					  "agility":10,
					  "willpower":10,
					  "career":"Warrior",
					  "weapon":"sword",
					  }
		self.myrole = role(properties)

	def init_role(self, role):
		"""init the role's properties """
		marks = 0  #marks decide the role's career and weapon
		try:
			print "Which way would you prefer in a fight?"
			marks += int(raw_input("1: melee combat. 2:hit and run. 1 or 2?\n"))

			print "Do you believe magic?"
			marks += int(raw_input("1: Never.      2: Yes.\n"))

			print "Do you think bow is a dirty weapon?"
			marks += int(raw_input("1: Yes.      2: No.\n"))

			print "What's the most important thing in fight?"
			marks += int(raw_input("1: Courage.      2: Intelligence\n"))

			print "Which kind of weapon would you prefer?"
			marks += int(raw_input("1: Sword.      2: Wund\n"))

		except ValueError:
			print "error input, please enter number!"
			return 'init_role'

		#set role's properties according to the marks
		if marks in [5,6]:
			role.career = "Warrior"
			role.strength = randint(15,19)
			role.willpower = randint(1,5)
			role.agility = 30 - role.strength - role.willpower
			if role.strength == 19:
				role.weapon = "harmmer"
			else:
				role.weapon = "sword"
			print "Honour is your life, great warrior!"
		elif marks in [7,8]:
			role.career = "Ancher"
			role.agility = randint(14,18)
			role.willpower = randint(2,6)
			role.strength = 30 - role.agility - role.willpower
			role.weapon = "bow"
			print "Hit and Run, you're really fight master, my ancher."
		else:
			role.career = "Wizard"
			role.willpower = randint(15,19)
			role.strength = randint(1,5)
			role.agility = 30 - role.willpower - role.strength
			role.weapon = "Wund"
			print "Magic is everything, noble wizard!"

		print "Now, start your advanture, my %s !" % role.career
		raw_input("The first mission is Valley, please press Enter to start.")
		return 'valley'

	def play(self):
		next_mission_name = 'init_role'
		while 1:
			print "\n*********************"
			mission = getattr(self,next_mission_name)
			next_mission_name = mission(self.myrole)
	
	def fight(self, role):
		role.attack()


	def valley(self, role):
		print "Here is valley, a gaint's manor"
		print "Would you want to pass through this valley over the gaint's body?"
		print "Or just try your luck, play dice with he?"
		try:
			decide = int(raw_input("1: fight.      2: play dice.\n"))
		except ValueError:
			print "Only input 1 or 2 please!"
			return 'valley'
		if decide == 1:
			print "just figth"
			for x in xrange(10):
				print role.attack()
		else:
			if role.luck > 7:
				print "Are you kidding me? Luck point %d" % role.luck
				print "The gaint won't play with such a luck guy, just go!"
			else:
				print "Roll your dice!"
				raw_input("press Enter to start roll!")
				yourpoint = randint(1,6)
				print "You got %d points" % yourpoint
				print "It's the gaint's turn now"
				raw_input("press Enter to continue")
				G_point = randint(1,6)
				print "The gaint got %d points." % G_point
				if yourpoint > G_point:
					print "you win! just go to next mission, luck guy!"
					raw_input("press Enter to go to dark jungle")
				else:
					print "Loser, you will be the gaint's meal."
					return 'death'
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
			self.hp = 1200
		elif self.career == "Archer":
			self.hp = 1000
		else:
			self.hp = 900
	

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
			print "miss! make no damage"
		else:
			print "You make %.1f points damage" % damage
		return damage

class monster(object):
	def __init__(self,name):
		"""set the monster's properties"""
		if name == "gaint":
			self.hp = 1200
			self.max_damage = 40
			self.unique_skill = "Frenzy Strike"
			self.us_damage = 80
		elif name == "evil wizard":
			self.hp = 800
			self.max_damage = 50
			self.unique_skill = "Ice Blast"
			self.us_damage = 120
		elif name == "dragon":
			self.hp = 1500
			self.max_damage = 60
			self.unique_skill = "True Dragon Fire"
			self.us_damage = 200
	
	def attack(self):
		"""define the monster's attack, return the damage value"""
		damage = 0






MyGame = game()
MyGame.play()
