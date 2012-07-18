#!/usr/bin/python
## A simple Game about magic and sword, enjoy it!
from random import randint
from time import sleep
import sys

class Game(object):

	def __init__(self):
		"""create a Game and show some welcome words"""
		print "Welcome to the world of sword and magic!"
		print "As the chosen one, you have to begin your advanture now!"
		print "Willing or not, you must do something, or you will never get back home."
		raw_input("Press 'Enter' to start advanture.")
		print "\n"


	def play(self):
		""" main method to process the Game """

		print "First, you will have a test to decide your career."
		raw_input("Press 'Enter' to begin the test!")
		print "\n"
		self.test_decide_Role()   #invoke the test to create a Role.
		print "Now, start your advanture, my %s !" % self.myRole.career
		raw_input("The first mission is Valley, please press Enter to start.")
	
		next_mission_name = 'valley'
		while 1:
			print "\n*********************"
			mission = getattr(self,next_mission_name)
			next_mission_name = mission(self.myRole)


	def get_marks(self, choices):
		while 1:
			mark = raw_input(choices)
			if mark == '2' or mark == '1':
				return int(mark)
			else:
				print "!"*32
				print "Error input!!!!!! please enter 1 or 2 only!"
				print "You need to make the choice again.\n"


	def test_decide_Role(self):
		"""take a test and create a Role for this Game according to the test result."""
		print "*"*32

		marks = 0  #marks decide the Role's properties
		print "Which way would you prefer in a fight?"
		marks += self.get_marks("1: melee combat. 2:hit and run. 1 or 2?\n")

		print "Do you believe magic?"
		marks += self.get_marks("1: Never.      2: Yes.\n")

		print "Do you think bow is a dirty weapon?"
		marks += self.get_marks("1: Yes.      2: No.\n")

		print "What's the most important thing in fight?"
		marks += self.get_marks("1: Courage.      2: Intelligence\n")

		print "Which kind of weapon would you prefer?"
		marks += self.get_marks("1: Sword.      2: Wund\n")

		self.myRole = Role(marks)


	def fight(self, Role, Monster):
		""" define the figth process between Role and Monster,
		    it won't be over until one side bleeds up his HP"""
		Role_damage = 0
		Monster_damage = 0
		print "This a fight between %s and %s" % (Role.career, Monster.name)
		raw_input("Press Enter to begin your fight with "+Monster.name+" !!!")
		while 1:
			if Role_damage >= Monster.hp:
				print "You Win! %s" % Role.career
				print "your total damage: ", Role_damage
				print "Monster total damage: ", Monster_damage
				break
			
			if Monster_damage >= Role.hp:
				print "You lose this fight, %s" % Role.career
				print "your total damage: ", Role_damage
				print "%s total damage: %d " % (Monster.name, Monster_damage)
				return 'lose'
			sleep(1)
			print ">>>>>>>>"
			Role_damage += Role.attack()
			sleep(1)
			print ">>>>>>>>"
			Monster_damage += Monster.attack()


	def death(self, Role):
		quips = [
			"Now or never, sorry you failed!",
			"It's not always the hero win the Game",
			"Do you really try your best?",
			"Whatever, try again, you may win next time."
		]
		print quips[randint(0, len(quips)-1)]
		print "You could have been a great " + Role.career
		exit(0)


	def valley(self, Role):
		""" to pass through the valley, you need to win a Game against gaint,
		    you could fight with him, or play dice with him, it depends on 
			your choice."""
		print "Here is valley, a gaint's manor"
		print "Would you want to pass through this valley over the gaint's body?"
		print "Or just try your luck, play dice with he?"
		try:
			decide = int(raw_input("1: fight.      2: play dice.\n"))
		except ValueError:
			print "Only input 1 or 2 please!"
			return 'valley'
		if decide == 1:
			gaint = Monster('Gaint')
			if self.fight(Role,gaint) == 'lose':
				return 'death'
		else:
			if Role.luck > 7:
				print "Are you kidding me? Luck point %d" % Role.luck
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
		print "Pass through the valley, next mission is dark jungle"
		raw_input("Pree Enter to the next mission.")
		return 'jungle'


	def jungle(self, Role):
		""" Dark jungle lives a evil wizard, if you could answer his riddle,
		    you could pass through the jungle safely, or you have to get 
			through over this evil guy's body"""
		print "Welcome to the dark jungle, there lives a evil wizard"
		print "How would you like to challenge the Evil Wizard --- Jig Saw ?"
		print "Try to solve his riddle or taste his black magic? Make your choice!!!"
		try:
			decide = int(raw_input("1: Let's see who is smarter.      2: Black magic is nothing.\n"))
		except ValueError:
			print "Only input 1 or 2 please!"
			return 'jungle'
		if decide == 1:
			riddle = ["What has six faces but does not wear makeup?\n It also has twenty-one eyes but cannot see.",
					  "It stands on one leg with its heart in its head.\n What is it?",
					  "What holds water yet is full of holes?",
					  "What fastens two people yet touches only one?",
					  "The more you have of it, the less you see. What is it?",
					  ]
			answer = ["dice","cabbage","sponge","wedding ring","darkness"]
			riddle_index = randint(0,len(riddle)-1)
			print "The riddle is: "
			print riddle[riddle_index]
			your_answer = raw_input("Your answer>>>")
			if your_answer == answer[riddle_index]:
				print "It seems you are not so stupid.\nMay the dargon will enjoy fresh meat, leave my jungle now, lad! "
				return 'castle'
			
		elif decide == 2:
			print "You will see what is really darkness."
			Evil_Wizard = Monster("Evil Wizard")
			if self.fight(Role, Evil_Wizard) == 'lose':
				return 'death'
		print "You are a man with light in heart even in darkness, you win!"
		raw_input("Pree Enter to the next mission.")
		return 'castle'


	def castle(self, Role):
		""" Powerful dragon is the last Monster you need to face, there is no
		    other way rather than fightting could pass through it, so prepare
			yourself, and make the final fight """
		print "Lo and behold, you get to the dragon's castle"
		print "The Dragon is not sleeping as usual, he begins to speak."
		sleep(2)
		print "@Dragon: Would you want to fight with a dragon, the most powerful creature?"
		sleep(2)
		print "@Dragon: Or you just want to get back home? It's very easy for a dargon."
		sleep(2)
		print "@Dragon: You will be home right away, in return, I need your weapon to expand my personal treasure-house"
		sleep(3)
		print "@Dragon: Make a quick choice, don't make a dragon wait."
		raw_input('???')
		print "1: abandon weapon and go home.    2. fight anyway."
		decide = raw_input(">>>")
		if decide == '1':
			print "@Dragon: It's really a good %s." % Role.weapon
			sleep(2)
			print "@Dragon: Stupid worm, go to the hell to find your home!!!"
			sleep(3)
			print "............."
			print "You are screwed by a dragon......"
			return 'death'
		else:
			print "@Dragon: You will see a dragon's wrath, worm."
			Dragon = Monster("Dragon")
			if self.fight(Role, Dragon) == 'lose':
				return 'death'
		print "*********************************************"
		print "*       WELCOME  BACK  HOME, WINNER!        *"
		print "*Life is a continuous fight that never ends!*"
		print "*It sucks, but enjoy it......               *"
		print "*********************************************"
		exit(1)



class Role(object):
	"""basic Role with properties and actions"""

	def __init__(self, marks):
		""" set the Role's basic properties depend the marks in test"""

		if marks in [5,6]:
			self.career = "Warrior"
			self.strength = randint(15,19)
			self.willpower = randint(1,5)
			self.agility = 30 - self.strength - self.willpower
			self.hp = 600
			self.skill = "Double Strike"
			self.sk_damage = 90
			if self.strength == 19:
				self.weapon = "Harmmer"
			else:
				self.weapon = "Sword"
			print "Honour is your life, great warrior!"
		elif marks in [7,8]:
			self.career = "Ancher"
			self.agility = randint(14,18)
			self.willpower = randint(2,6)
			self.strength = 30 - self.agility - self.willpower
			self.weapon = "Bow&Arrow"
			self.hp = 500
			self.skill = "Fatal Arrow"
			self.sk_damage = 100
			print "Hit and Run, you're really fight master, my ancher."
		else:
			self.career = "Wizard"
			self.willpower = randint(15,19)
			self.strength = randint(1,5)
			self.agility = 30 - self.willpower - self.strength
			self.weapon = "Wand"
			self.hp = 400
			self.skill = "God's Thunder"
			self.sk_damage = 120
			print "Magic is everything, noble wizard!"
		self.luck = randint(1,10)
		print "*********************************************"
		print "*   Career: %s               " % self.career
		print "*   Weapon: %s               " % self.weapon
		print "*    Skill: %s               " % self.skill
		print "*HP points: %d               " % self.hp
		print "* Strength: %d               " % self.strength
		print "*  Agility: %d               " % self.agility
		print "*Willpower: %d               " % self.willpower
		print "*     Luck: %d               " % self.luck
		print "*********************************************"


	def attack(self):
		"""attack method return damage value depending on career"""

		if self.career == "Warrior":
			damage = 1.8*self.strength + 1.2*self.agility + 0.6*self.willpower + randint(0, 2*self.luck)
		elif self.career == "Archer":
			damage = 1.2*self.strength + 2.0*self.agility + 0.4*self.willpower + randint(0, 2*self.luck)
		else:
			damage = 0.6*self.strength + 0.8*self.agility + 2.4*self.willpower + randint(0, 2*self.luck)

		if randint(0, self.agility) == 0:
			damage = 0
			print "Miss! You make no damage."
		elif randint(1,4) == 3:
			damage = self.sk_damage + randint(0,self.luck)
			print "You launch you speciall skill: %s !" % self.skill
			print "***That makes %d ponits damage, cool!" % damage
		else:
			print "You hit it and  make %.1f points damage" % damage
		return damage



class Monster(object):
	def __init__(self,name):
		"""set the Monster's properties"""
		if name == "Gaint":
			self.hp = 600
			self.name = name
			self.max_damage = 70
			self.unique_skill = "Frenzy Strike"
			self.us_damage = 80
			self.hit_rate = 5
			self.skill_rate = 6
		elif name == "Evil Wizard":
			self.hp = 400
			self.name = name
			self.max_damage = 50
			self.unique_skill = "Ice Blast"
			self.us_damage = 120
			self.hit_rate = 8
			self.skill_rate = 5
		elif name == "Dragon":
			self.hp = 700
			self.name = name
			self.max_damage = 60
			self.unique_skill = "True Dragon Fire"
			self.us_damage = 150
			self.hit_rate = 7
			self.skill_rate = 3


	def attack(self):
		"""define the Monster's attack, return the damage value"""
		damage = 0
		if randint(1,10) > self.hit_rate:
			print "%s missed this attack, good luck!" % self.name
		else:
			if randint(1,10) < self.skill_rate:
				print "%s use his unique skill: %s !!!" % (self.name, self.unique_skill)
				damage = self.us_damage - randint(0,20)
				print "###That make %d points damage, damn it!" % (damage)
			else:
				damage = self.max_damage - randint(0,10)
				print "%s hit you and make %d points damage" % (self.name,damage)
			 
		return damage


if __name__ == '__main__':
	MyGame = Game()
	MyGame.play()
