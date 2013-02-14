#!/usr/bin/python
from datetime import date
now = date.today()
print "The date today: " + str(now)
birthday = date(1988,2,23)
print "Birthday: " +str(birthday)
age = now - birthday
print "The days you have lived: " + str(age)
left = date(2068,2,23) - now 
print "The days you left are: " + str(left)
