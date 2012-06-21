#!/usr/bin/python
"""queens' question'"""
def conflict(state,nextX):
	nextY = len(state)
	for i in range(nextY):
		if abs(state[i]-nextX) in (0,nextY-i):
			return True
	return False

def queens(num=8, state=()):
	for pos in range(num):
		if not conflict(state,pos):
			if len(state) == num-1:
				yield(pos,)
			else:
				for result in queens(num,state + (pos,)):
					yield(pos,) + result

def prettyprint(solution):
	def  line(pos,length=len(solution)):
		return "0"*(pos) + 'X' +"0"*(length-pos-1)
	for pos in solution:
		print line(pos)

print list(queens(4))
for i in range(len(list(queens(4)))):
	prettyprint(list(queens(4))[i])
	print "@@@@@@@@"
#print list(queens(3))
#print list(queens(4))
#print len(list(queens(5)))
