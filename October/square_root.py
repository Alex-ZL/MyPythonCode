# coding: utf-8
def square_root(x, epsilon):
    step = epsilon**2
    numGuesses = 0
    ans = 0.0
    while(abs(ans**2 - x)) > epsilon and ans <= x:
        ans += step
        numGuesses += 1
    print "numGuesses = ", numGuesses
    if abs(ans**2-x) >= epsilon:
        print "Failed on square root of %r" %x
    else:
        print "%r is close to the square root of %r" %(ans, x)
        
print square_root(35, 0.1)
