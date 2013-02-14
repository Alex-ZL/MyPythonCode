#!usr/bin/env python
def iterPower(base, exp):
	result = 1
	while exp > 0:
		result *= base
		exp -= 1
	return result

def recurPower(base, exp):
	if exp == 0:
		return 1
	else:
		return base*recurPower(base, exp-1)
print iterPower(2,10)
print recurPower(3,10)
strs = "whatever"
tts = "whatever"
print strs[3]
print strs[4:]
print strs==tts
