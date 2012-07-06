class wired_return(object):
	def __init__(self,start):
		self.start = start

	def fun(self):
		print "Here is fun"
		what = getattr(self,self.start)
		ever = what()


	def fun1(self):
		print "Here is fun1"
		return 'fun2'

	def fun2(self):
		print "Fun2"

a_fun = wired_return('fun1')
print a_fun.fun1()
