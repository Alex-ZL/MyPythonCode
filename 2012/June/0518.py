#! /usr/bin/python
#import this """display zen of python"""
import Tkinter
class test_magicmethod:
	def __init__(self,test):
		print "init"+ test

test = test_magicmethod(" magic")
