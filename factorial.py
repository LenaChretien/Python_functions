def factorial(num):
    """
    Given some real number, return the factorial of that number.
    
    Args:
    num: A real positive number -> int
    
    Return:
    The factorial of that number
    """
    # Base case
    if num in [0, 1]:
        return 1
    
    # Recursive call
    return num * factorial(num-1)
    
    
  
  
def factorial_nonrecur(num):
    if num in [0, 1]:
        return 1
    
    prod = 1
    while num > 1:
        prod *= num
        num -= 1
        
    return prod