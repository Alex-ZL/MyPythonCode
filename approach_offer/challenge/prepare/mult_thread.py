#!/usr/bin/env python
## a example for multiple threads
import time
from threading import Thread
import Queue

class Worker(Thread):
	def __init__(self, name, worklist,outlist):
		Thread.__init__(self)
		self.worklist = worklist
		self.name = name
		self.start()
		self.outlist = outlist
		
	def run(self):
		while 1:
			if self.worklist.empty():
				break

			cur_work = self.worklist.get()

			time.sleep(1)

			print self.name, "working on NO.", cur_work, " task" 

			time.sleep(1)
			self.outlist.put(cur_work+self.name)

			print self.name, "has finished NO.", cur_work, " task"

			self.worklist.task_done()


def Launch(url_list):
	worklist = Queue.Queue()
	outlist = Queue.Queue()
	
	for item in url_list:
		worklist.put(item)
	
	for i in range(2):
		threadName = "Thread" + str(i)
		Worker(threadName, worklist, outlist)
	
	worklist.join()
	return outlist

url_list = ['1 baidu', '2 sohu', '3 ctrip', '4 google', '5 facebook', '6 everNote']
result = Launch(url_list)
while result.empty() == False: 
	item = result.get()
	print item
