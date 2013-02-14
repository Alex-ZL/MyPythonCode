#!/usr/bin/python
d = {}
f = open('/home/alex/MyPython/input.txt')
str = f.read()
for s in str:
	if d.has_key(s):
		d[s] +=1
	else: d[s] = 1
f.close

##for k,v in d.items():
##	print "%s : %s" %(k,v)
print ''.join([c for c in str if c.isalpha()])
