#!/usr/bin/env python
def isIn(char, aStr):
	count = len(aStr)
	if count == 0:
		return False
	elif count == 1:
		return char == aStr
	else:
		pos = count/2
		if char == aStr[pos]:
			return True
		elif char < aStr[pos]:
			return isIn(char, aStr[:pos])
		else:
			return isIn(char, aStr[pos+1:])

print isIn("c", "abcdef")
