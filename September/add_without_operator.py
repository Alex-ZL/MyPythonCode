#/usr/bin/env python
#coding: utf-8

def newadd(x, y):
	if not y:
		return x
	sum0 = x^y
	temp = (x>y)<<1
	return newadd(sum0, temp)

def newadd2(x, y):
	while 1:
		a = x&y
		b = x^y
		x = a << 1
		y = b
		if a == 0:
			break
	return b

if __name__=='__main__':
	a = int(raw_input("enter the first number: "))
	b = int(raw_input("enter the second number: "))
	print newadd2(a,b)
