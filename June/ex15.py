#!/usr/bin/python
from sys import argv

#get script and input file names by unpack two strings
script, filename = argv

#open the input file
txt = open(filename)

#print the input file name and it's content.
print "Here's your file %r:" %filename
print txt.read()

txt.close()

#prompt to get another plain file.
print "Type the filename again:"
file_again = raw_input(">")

#open the file just input according to the file name.
txt_again = open(file_again)

#print out the content of the file.
print txt_again.read()
txt_again.close()
