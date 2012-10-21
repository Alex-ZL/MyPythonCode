# coding: utf-8
def square_root2(x,epsilon):
    numGuesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low)/2.0
    while abs(ans**2 - x) >= epsilon:
        numGuesses += 1
        if ans**2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print "numGuesses = %r" %numGuesses
    print ans, "is close to suqare root of", x
    