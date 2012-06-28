#!/usr/bin/python
## exercise 33

i = 0
l = int(raw_input("Enter the loop times: "))
step = int(raw_input("Enter the step: "))
numbers = []

while i < l:
	 print "At the top i is %d" %i
	 numbers.append(i)

	 i = i + step
	 print "Numbers now: ", numbers
	 print "At the bottom i is %d" %i

print "The numbers: "

for num in numbers:
	print num

xlist= [1,2,3,4]
y = int(raw_input(">"))
if y not in xlist:
	print "Damn it!"
