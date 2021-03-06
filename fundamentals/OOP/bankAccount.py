
class BankAccount:
    def __init__(self, name, int_rate, deposit, withdraw, balance):
        self.name = name
        self.intRate = int_rate
        self.deposit = deposit
        self.withdraw = withdraw
        self.balance = balance

    def depositMoney(self, amount):
        if amount > 0:
            self.balance += amount
            return self

    def withdrawMoney(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self

    def displayBalance(self):
        print(self.balance)
        return self


    def yield_interest(self):
        self.balance = self.balance + (self.balance * self.intRate)
        return self

class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount(int_rate = 0.01, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self


bob = BankAccount('Bob', .1, 0, 0, 0)
tom = BankAccount('Tom', .1, 0, 0, 0)
jon = BankAccount('Jon', .1, 0, 0, 0)

bob.depositMoney(105).depositMoney(100).depositMoney(100).withdrawMoney(50).displayBalance().yield_interest()
tom.depositMoney(75).depositMoney(450).withdrawMoney(25).withdrawMoney(40).withdrawMoney(30).withdrawMoney(60).yield_interest().displayBalance()
print(bob.balance)
