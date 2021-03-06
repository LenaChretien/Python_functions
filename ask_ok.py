def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = input(prompt)   # In Python 2, it is called raw_input()
        if ok in ['y', 'ye', 'yes']:
            return True
        if ok in ['n', 'no', 'nop', 'nope']:
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('Not a good user.')
        print(complaint)