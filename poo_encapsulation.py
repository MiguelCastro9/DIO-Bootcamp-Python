# POO - encapsulation in python

# in encapsulation in python we cannot exactly define the conventional form of encapsulation,
# but we have a conventional rule defined by _ that symbolizes the private attribute and when we don't use _ the attributes are public.
class Account:
    def __init__(self, nr_agency, balance=0):
        self._balance = balance
        self.nr_agency = nr_agency

    def deposit(self, value):
        self._balance += value
    
    def withdraw(self, value):
        self._balance -= value

    def show__balance(self):
        return self._balance
    
account = Account("0001", 100)
account.deposit(100)
print(account.nr_agency)
print(account.show__balance())