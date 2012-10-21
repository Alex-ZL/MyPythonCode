# 6.00x Problem Set 3
#
# Successive Approximation: Newton's Method
#


# Problem 1: Polynomials
def evaluatePoly(poly, x):
    '''
    Computes the value of a polynomial function at given value x. Returns that
    value as a float.
 
    poly: list of numbers, length > 0
    x: number
    returns: float
    '''
    polynomial = 0.0
    for i in range(len(poly)):
        polynomial += poly[i] * (x**i)
    return polynomial



# Problem 2: Derivatives
def computeDeriv(poly):
    '''
    Computes and returns the derivative of a polynomial function as a list of
    floats. If the derivative is 0, returns [0.0].
 
    poly: list of numbers, length &gt; 0
    returns: list of numbers (floats)
    '''
    deriv = []
    for i in range(1,len(poly)):
        deriv.append(poly[i]*float(i))
    if not deriv:
        deriv.append(0.0)
    return deriv

print computeDeriv([-13.39,0.0,17.5,3.0,1.0])
print computeDeriv([6,1,3,0])
print computeDeriv([20])





# Problem 3: Newton's Method
def computeRoot(poly, x_0, epsilon):
    '''
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a list containing the root and the number of iterations required
    to get to the root.
 
    poly: list of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: list [float, int]
    '''
    # FILL IN YOUR CODE HERE...
    deriv = computeDeriv(poly)
    count = 0
    x = x_0
    while abs(evaluatePoly(poly,x)) > epsilon:
        x = x -evaluatePoly(poly,x)/evaluatePoly(deriv,x)
        count += 1
    return [x,count]
poly = [-13.39, 0.0, 17.5, 3.0, 1.0]
x_0 = 0.1
epsilon = .0001
print computeRoot(poly, x_0, epsilon)
print computeRoot([-13.39,0.0,17.5,3.0,1.0],0.1,0.0001)
