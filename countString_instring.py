import re

def countString(raw_string, string_to_count):
    '''
    raw_string: a string
    string_to_count: a string to be counted
    
    returns: a positive number which is number of times that string_to_count occurs in raw_string.
    '''
    # Your code here
    if len(string_to_count) == 0:
        raise ValueError('The length should not be 0!')
    elif len(raw_string) < len(string_to_count):
        result = 0   
        
    else:
        result = len(re.findall(string_to_count,raw_string))
    return result
