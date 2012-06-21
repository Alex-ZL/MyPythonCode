#!/usr/bin/python
import string

file = open("input")
outfile = open("output","w")
checkfile = open("file_need_check")
x_list = []
out_list = []
for line in file:
	pos=string.find(line,"BM*")
	#print line[19:27]+line[pos+3:pos+12]
	x_list.append(line[19:27]+line[pos+3:pos+12])
	
for element in x_list:
	if element not in out_list:
		out_list.append(element)

for line in checkfile:
	#print line[:17]
	if line[:17] not in out_list:
		print "Not match"

sorted(out_list,reverse=True)

for item in out_list:
	outfile.write("%s\n" %item)
