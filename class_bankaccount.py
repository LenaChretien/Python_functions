# Make class BankAccount with attributes deposit, withdraw check_balance
class BankAccount(object):
    # Your code here
    def __init__(self, name, balance):
        self._balance = balance
        self._name = name
    
    def deposit(self,n):
        self._balance += n
        return self._balance
    
    def withdraw(self,n):
        if n > self._balance:
            raise ValueError("You don't have enough money for this transaction")
        self._balance -= n
        return self._balance
    
    def check_balance(self):
        print(self._balance)
        