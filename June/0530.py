#!/usr/bin/python
## challenge 3
import re
p = re.compile('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]')

f = open('/home/alex/MyPython/input2.txt')
str = f.read()
f.close()

d = []
for s in p.findall(str):
	d.append(s[4])
print ''.join(d)
print len(p.findall(str))
