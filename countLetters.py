def countLetter(raw_string):
    '''
    raw_string: a string
    
    returns: a dict contains each letter and it's corresponding frequency
    '''
    # Your code here
    import re
    from collections import Counter
    letters = re.findall('[a-z]',raw_string.lower())
    Counter(letters)


    
    ## Version two
    def countLetter(raw_string):
    '''
    raw_string: a string
    
    returns: a dict contains each letter and it's corresponding frequency
    '''
    # Your code here
    lower_string = raw_string.lower()
    alphabet = [chr(i) for i in range(97, 123)]
    count_dict = {}
    for letter in lower_string:
        if letter in alphabet:
            if letter in count_dict.keys():
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1
    return count_dict