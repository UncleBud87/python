
class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.intRate = int_rate

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

    def depositMoney(self, amount):
        self.account.depositMoney(amount)
        return self

    def withdrawMoney(self, amount):
        self.account.withdrawMoney(amount)
        return self

    def displayBalance(self):
        self.account.displayBalance()
        return self

    def yield_interest(self):
        self.yield_interest()
        return self

bob = User("Bob")
tom = User("Tom")

bob.depositMoney(105).depositMoney(100).depositMoney(100).displayBalance()