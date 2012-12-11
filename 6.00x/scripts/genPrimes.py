def gen_primes():
	"""Generates successive prime numbers every time it's called."""
	yield 2
	yield 3
	prime_list = [2, 3]
	while 1:
		next = prime_list[-1] + 2
		i = 0
		while i < len(prime_list):
			if next%prime_list[i] == 0:
				next+=2
				i=0
			else:
				i+=1
		prime_list.append(next)
		yield next

prime = gen_primes()
for x in xrange(20):
	print prime.next()
