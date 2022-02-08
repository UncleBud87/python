class BankAccount:
# don't forget to add some default values for these parameters!
    def __init__(self, int_rate, deposit, withdraw, balance): 
        self.int_rate = int_rate
        self.deposit = deposit
        self.withdraw = withdraw
        self.balance = balance
# your code here! (remember, instance attributes go here)
# don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        if amount > 0:
            self.deposit = amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.withdraw = -amount

    def display_account_info(self):
        print (self.balance)
# your code here
    def yield_interest(self):
# your code here
