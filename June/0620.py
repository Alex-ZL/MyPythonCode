#!/usr/bin/python
## type some codes from Learn Python The Hard way ex10.
print "I am 6'2\" tall."
print 'I am 6\'2" tall'

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print "what's the differenct between %r and %s?" %(tabby_cat, tabby_cat)

#print "How old are you?",
#age = raw_input()
#print "How tall are you?",
#height = raw_input()
#print "How much do you weight?",
#weight = raw_input()
#
age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weight?")
print "So, you're %r old, %r tall and %r heavy." %(age, height,weight)


