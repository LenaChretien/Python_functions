def replacefirst(L, v):
    ''' Replaces the first element of a list
    
    Args: a list and an integer.
    
    Return: list with first element replaces by v
    
    '''
    return [v] + L[1:]
