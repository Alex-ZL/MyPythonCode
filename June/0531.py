#!/usr/bin/python
## Concise, recursive and with list comprehension
import string
f = open('/home/alex/MyPython/input2.txt')
f = f.read()
markers = ''.join(['1' if c in string.uppercase else '0' for c in f])
def fun(res, t2, markers):
	n = len(markers.partition('011101110')[0])
	return fun( res+t2[n+4], t2[n+9:], markers[n+9:] ) if n != len(markers) else res

teststr = "whatsUPMaNYOuneedMORePASsion"
testMarkers = ''.join(['1' if c in string.uppercase else '0' for c in teststr])
print fun('',teststr,testMarkers)
print fun('',f, markers)
