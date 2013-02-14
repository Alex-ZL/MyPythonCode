#!/usr/bin/env python

import sys
import pprint

def test(*args, **kwargs):
	print args
	print kwargs
	raise Exception("Error!")

def main():
	test(1,'a', x=10)

if __name__ == "__main__":
	main()
