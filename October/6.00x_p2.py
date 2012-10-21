#!/usr/bin/env python
balance = 5000
annualInterestRate = .18
monthlyPaymentRate = .02
monthlyInterestRate = .18/12
total_paid = 0
for i in xrange(1,13):
	print "Month: %d" %i
	mini_monthly_payment = balance * monthlyPaymentRate
	print "Minimum monthly payment: %.2f" %round(mini_monthly_payment)
	balance = (balance - mini_monthly_payment)*(1+monthlyInterestRate)
	print "Remaining balance: %.2f" %round(balance)
	total_paid += mini_monthly_payment

print "Total paid: %d" %round(total_paid)
print "Remaining balance: %d" %round(balance)


print "round output %r" %round(balance)
print round(balance)
