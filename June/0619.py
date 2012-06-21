#!/usr/bin/python
## Learn python the hard way, ex6
x = "There are %d types of people." % 10 #set a variable x
binary = "binary" #set variable binary
do_not = "don't" #set variable do_not
y = "Those who know %s and those who %s." %(binary, do_not) #combine two words into a sentence

print x 
print y #print out what I said

print "I said: %r." % x #requote what I said
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation %hilarious #print two string in another way.
w = "This is the left side of..."
e = "a string with a right side."

print w+e #combine two sentences

print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "."*10 #print 10 astrisks.

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1+end2+end3+end4+end5+end6, #cancatenate end1-6 strings
print end7+end8+end9+end10+end11+end12

print "*"*16

formatter = "%r %r %r %r"
print formatter %(1, 2, 3, 4)
print formatter %("one", "two", "three", "four")
print formatter %(True, False, True, False)
print formatter %(formatter, formatter, formatter, formatter)
print formatter %(
		"I had this thing.",
		"That you could type up right.",
		"But it didn't sing.",
		"So I sing it myself."
		)


print "*"*16

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lins if we want, or 5, or 6.
"""
#next go to Ex 10
