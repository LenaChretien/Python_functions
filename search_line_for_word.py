def search(keyword, filename):
'''
- takes keyword and dame of a file
- opens the file and iterates through the file object line by line. If you find the keyword in the line, it iw yield

'''
    rows = [lines for lines in open(filename) if keyword in lines]
    yield rows 