def reverseString(raw_string):
'''
Function will take a string and returns a new string, that is reversed word by word

Args: String

Rets: string in reversed order
'''
    jo = " ".join(raw_string.split()[::-1])
    return print(jo)