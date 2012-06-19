#!/usr/bin/python
## Fibonacci numbers for python debug exercise

def main():
	low, high = 0, 1
	for i in xrange(10):
		print high
		low, high = high, low + high

if __name__ == '__main__':
	main()
