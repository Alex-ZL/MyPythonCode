#!/usr/bin/env python
import unittest

class DefaultTestCase(unittest.TestCase):
	def setUp(self):
		self.what = 'ever'

	def tearDown(self):
		self.what = ''
	
	def testrun1(self):
		#self.assert_(self.what == 'foo', 'incorrect default size')
		assert self.what == 'for', 'failed testRun1'

	def testrun2(self):
		self.assert_(self.what == 'ever', 'incorrect answer 2')


unittest.main()
