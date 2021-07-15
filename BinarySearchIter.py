# The bisection method in mathematics is a root-finding method that repeatedly bisects an interval and then selects a subinterval in which a root must lie for further processing.

#Given a continuous function f and an interval [𝑎,𝑏], which satisfies that the values of 𝑓(𝑎) and 𝑓(𝑏) are opposite, say 𝑓(𝑎)∗𝑓(𝑏)<0 (there is at least one zero crossing within the interval).

# Calculate 𝑐, the midpoint of the interval, 𝑐=0.5∗(𝑎+𝑏).
# Calculate the function value at the midpoint, 𝑓(𝑐)
# If convergence is satisfactory (that is, 𝑓(𝑐) is sufficiently small), return 𝑐 and stop iterating.

def binarySearchIter(fun, start, end,  eps=1e-10):
    '''
    fun: funtion to fund the root
    start, end: the starting and ending of the interval
    eps: the machine-precision, should be a very small number like 1e-10
    
    return the root of fun between the interval [start, end]
    '''
    if fun(start) * fun(end) >= 0:
            raise ValueError('The sign of fun(start) and fun(end) should be opposite!')
    
    c = (start + end)/2.0
    
    while abs(fun(c)) > eps:
        if fun(start)*fun(c) > 0:
            start = c
        else:
            end = c
        c = (start + end)/2.0
    return c