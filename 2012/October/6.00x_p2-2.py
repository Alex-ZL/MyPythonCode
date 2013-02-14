#!/urs/bin/env python
balance = 320000
annualInterestRate = 0.2
lowest_payment = 0
rate = 1+annualInterestRate/12
lo = balance/12
hi = balance*(rate**12)/12
rest = 0
while 1:
	lowest_payment = (lo+hi)/2
	rest = balance
	for i in xrange(12):
		rest = (rest - lowest_payment)* rate
	if rest>0.0001:
		lo = lowest_payment
	elif rest<-0.0001:
		hi = lowest_payment
	else:
		break
print "Lowest Payment: %.2f" %lowest_payment
