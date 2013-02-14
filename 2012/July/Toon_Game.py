#Going with the idea to plan first, code later
#i want a tiny RPG, with a character with stats.
#classes i'm going to use are character, battle, opponent, and room.
#there will be a few rooms to navigate between, and a few opponents in the room which can be chosen to battle. rooms will be grids of x*y size and with input there will be character movement. 
#when your character is adjacent to an opponent it'll fight it.

from random import randint,random
from time import sleep
from sys import exit

class character(object):
    """This is you. you have stats (variables) and battle moves (functions)"""
    def __init__(self, name, strenght, defense):
        self.name = name
        self.strenght = strenght
        self.defense = defense
        self.health = 2000
        self.x = -1
        self.y = -1
        
    
    def navigate(self,x,y,room):
        if x<0 or y<0:
            raise IndexError
        """navigate through or to any given coordinate in any room"""
        if room.cells[y][x] == ' ':
            try:
                room.cells[self.y][self.x] = ' '
            except IndexError:
                pass
            self.x = x
            self.y = y
            self.room = room
            room.cells[y][x] = self
            for cell in room.adjacent_cells(x,y):
                if str(type(cell)) == "<class '__main__.monster'>":
                    self.room.show()
                    fight = battle(self,cell,"Oh noes! a {opponent} attacks from the shadows!")
                    fight = fight.fight() #trololol
                    if fight == "win":
                        room.cells[cell.y][cell.x] = ' '
                    if fight == "loss":
                        print "You die. loser."
                        exit(0)
            return "success"
        else:
            return "fail"




class room(object):
    """mostly a list of cells with strings, monsters or your character in it"""
    def __init__(self,width,height,monsters):
        self.width = width
        self.height = height
        self.monsters = monsters
        self.cells = []
        for y in range(self.height):
            self.cells.append([])
            for x in range(self.width):
                self.cells[y].append(' ')
        for monster in monsters:
            self.cells[monster.y][monster.x] = monster
                
                
    def adjacent_cells(self,x,y):
        adj_cells = []
        if x == self.width-1:
            offsetx = range(-1,1)
        elif x == 0:
            offsetx = range(0,2)
        else:
            offsetx = range(-1,2)
        if y == self.height-1:
            offsety = range(-1,1)
        elif y == 0:
            offsety = range(0,2)
        else:
            offsety = range(-1,2)
        for dx in offsetx:
            for dy in offsety:
                if not dy == dx:
                    adj_cells.append(self.cells[y+dy][x+dx])

        return adj_cells
        
    def enter(self,player,x,y):
        self.player = player
        self.player.x = x
        self.player.y = y
        self.cells[y][x] = player
        
    def addmonsters(self,monsters):
        for monster in monsters:
            self.cells[monster.y][monster.x] = monster
    
    def addplayer(self,player):
        if self.cells[player.y][player.x] != ' ':
            self.cells[player.y][player.x] = player
        else:
            return "error"


    def show(self):
        """shows the room in the CLI
        player is a tuple of coordinates
        opponents is a list of tuples with coordinates
        """
        for line in self.cells:
            for cell in line:
                if str(type(cell)) == "<class '__main__.monster'>":
                    print "[x]",
                elif str(type(cell)) == "<class '__main__.character'>":
                    print "[o]",
                else:
                    print "[ ]",
            print "\n"
                
                
        

class battle(object):
    def __init__(self, player, opponent, reason):
        print reason.format(opponent = opponent.type)
        self.player = player
        self.opponent = opponent
        action = raw_input("What do you do next?\n\t1. fight\n\t2.\n\t3.\n> ")
        if "ight" in action or "1" in action:
            print "\nBring it on, bitch!\n"
            sleep(1)

    def fight(self):
        while self.player.health > 0 and self.opponent.health > 0:
            playeroption = randint(1,6)
            monsteroption = randint(1,3)
            nodamage = False
            if playeroption >= 2:
                print "{} attacks!".format(self.player.name)
                rndp = random()
                playerdamage = int(((float(self.player.strenght)/float(self.opponent.defense))*100)*rndp)
                self.opponent.health -= playerdamage
            elif playeroption == 1:
                print "{} dodges!".format(self.player.name)
                nodamage = True

            sleep(1)

            if monsteroption >= 2:
                print "{} attacks!".format(self.opponent.type)
                rndm = random()
                monsterdamage = int(((float(self.opponent.strenght)/float(self.player.defense))*100)*rndm)
                self.player.health -= monsterdamage

            elif monsteroption == 1:
                print "{} dodges!".format(self.opponent.type)
                if playeroption >= 2:
                    self.opponent.health += playerdamage
            if nodamage == True and monsteroption >= 2:
                self.player.health += monsterdamage

            sleep(1)

            if playeroption >= 2 and monsteroption >= 2:
                print "\t{player} damages {monster} for {damage}".format(player = self.player.name, monster = self.opponent.type,damage = playerdamage)
                print "\t{monster} damages {player} for {damage}".format(monster = self.opponent.type, player = self.player.name, damage = monsterdamage)
                print "\t\t\t\t{player} {phealth} || {mhealth} {monster}".format(player = self.player.name,phealth = self.player.health, mhealth = self.opponent.health, monster = self.opponent.type)
                
            elif monsteroption == 1 and playeroption >= 2:
                print "{player} misses!".format(player = self.player.name)
                
            elif monsteroption >= 2 and playeroption == 1:
                print "{monster} misses!".format(monster = self.opponent.type)
            else:
                print "\tWe're dancin'! woo!"
            print "\n-----------------\n"
            sleep(2)
        

        if self.player.health <= 0:
            return "loss"
        else:
            return "win"
                                                                      
        




class monster(object):
    """both for fights and rooms"""
    def __init__(self,x,y,room,mtype,STR,DEF,HP):
        #check if coords are taken
        allowed = True
        for monster in room.monsters:
            if (x,y) == (monster.x,monster.y):
                allowed = False
                break
            else:
                allowed = True
        if allowed == True:
            self.x = x
            self.y = y
            self.room = room
            self.type = mtype
            self.strenght = STR
            self.defense = DEF
            self.health = HP
        else:
            print "monster crashed"
            del self

    
        






print "\nWelcome! Let's make your character.\n"
name = raw_input("Name? > ")

strenght = randint(30,70)
defense = 100-strenght

print "\nyour STR is randomed at: {}. therefore your defense is: {}\n".format(strenght,defense)
player = character(name,strenght,defense)
print "Character made! let's get down to business. here is our newbie room:"

newb_room = room(10,10,[])

startmonsters = []
for x in range(5):
    startmonsters.append(monster(randint(0,newb_room.width-1),randint(0,newb_room.height-1),newb_room,'bat',50,25,400))
for x in range(2):
    startmonsters.append(monster(randint(0,newb_room.width-1),randint(0,newb_room.height-1),newb_room,'hound',100,25,500))
startmonsters.append(monster(randint(0,newb_room.width-1),randint(0,newb_room.height-1),newb_room,'justin bieber',0,1,1000))
newb_room.addmonsters(startmonsters)
newb_room.show()

print "an X means a monster. If you are at a cell next to a monster, you have to fight it."
print "at which cell do you want to place your character? (x,y)"

coordinates = raw_input("> ")
x, y = coordinates.strip('()').split(',')
x = int(x) - 1
y = 10-int(y)
while player.navigate(int(x),int(y),newb_room) == "fail":
    print "cannot navigate there!"
    coordinates = raw_input("> ")
    x, y = coordinates.strip('()').split(',')
    x = int(x) - 1
    y = int(y) - 1
newb_room.show()

#here is where the beginning ends and the repetitive part start

print "If you have not been attacked at your placement, i suggest moving next to a monster to fight it!"
print "\nEnter any sequence of WASD keys to move. For example: SD-<RETURN> should move you down once and then to the right once."



while True:
    
    seq = raw_input("> ")
    for letter in seq:
        try:
            if letter == "W" or letter == "w":
                player.navigate(player.x,player.y-1,newb_room)
            if letter == "A" or letter == "a":
                player.navigate(player.x-1,player.y,newb_room)
            if letter == "S" or letter == "s":
                player.navigate(player.x,player.y+1,newb_room)
            if letter == "D" or letter == "d":
                player.navigate(player.x+1,player.y,newb_room)
        except IndexError:
            newb_room.show()
            print "You run into a wall and die. Did you really think there was a door?"
            exit(0)
    newb_room.show()
    anymonsters = False
    for line in newb_room.cells:
        for cell in line:
            if str(type(cell)) == "<class '__main__.monster'>":
                anymonsters = True
    if anymonsters == False:
        print "\nYou've won! You've slaughtered all the monsters and i'm too lazy to make more content for you!"
        print "As a reward you may try walking out of the room, There will be piles of gold ready next door!"
    print "\nEnter any sequence of WASD keys to move."        
    
