class wired_return(object):
	def __init__(self,start):
		self.start = start

	def fun(self):
		print "Here is fun"
		what = getattr(self,self.start)
		ever = what()


	def fun1(self):
		print "Here is fun1"
		return 'fun'

	def fun2(self):
		print "Fun"

a_fun = wired_return('what do you want?')
a_fun.fun1()
