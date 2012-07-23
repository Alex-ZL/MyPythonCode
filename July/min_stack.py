#usr/bin/evn python
## simulate stack with min, push, pop O(1)

class stack(object):

	def __init__(self):
		self.values = []
		self.min_value = None

	def push(self, x):
		if self.min_value == None:
			self.min_value = x
		self.values.append(x-self.min_value)
		if x < self.min_value:
			self.min_value = x

	def pop(self):
		if len(self.values) == 0:
			print "stack is empty, pop nothing."
			exit(0)
		else:
			top = self.values.pop()
			if top >= 0:
				return top+self.min_value
			else:
				self.min_value -= top
				return self.min_value+top

	def opt_push(self, x):
		if self.min_value == None:
			self.min_value = x
		if x >= self.min_value:
			self.values.append(x)
		else:
			self.values.append(x*2-self.min_value)
			self.min_value = x
	
	def opt_pop(self):
		if len(self.values) == 0:
			print "stack is empty, pop nothing."
			exit(0)
		else:
			top = self.values.pop()
			if top >= self.min_value:
				return top
			else:
				temp = self.min_value
				self.min_value = 2*self.min_value - top
				return temp

if __name__ == '__main__':
	test_stack = stack()
	tlist = [2,3,-5,7,4,1]
	for item in tlist:
		test_stack.opt_push(item)
	for i in xrange(8):
		print "current min value in stack is ", test_stack.min_value
		print "stack pop value", test_stack.opt_pop()
