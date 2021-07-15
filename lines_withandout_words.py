def lines_withandout_words(file,word1,word2):
''' '''
    f = open(file, 'r')
    lines = f.readlines()
    outlines = [lines for lines in lines if word1 in lines and word2 not in lines ]
    return outlines
