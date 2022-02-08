class User:
    # class attributes get defined in the class
    bank_name = "First National Dojo"
    # now our method has 2 parameters!

    def __init__(self, name, email_address):
        # we assign them accordingly
        self.name = name
        self.email = email_address
        # the account balance is set to $0
        self.account_balance = 0

    def make_deposit(self, amount):    # takes an argument that is the amount of the deposit
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name} ,Balence {self.account_balance}")
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance = self.account_balance - amount
        other_user.account_balance = other_user.account_balance + amount
        return self


adrien = User("Adrien", "adrien@python.com")
nibbles = User("Mr. Nibbles", "nibbles@python.com")
benny = User("Benny Bob", "bennybob@python.com")

adrien.make_deposit(105).make_deposit(100).make_deposit(100).display_user_balance()
nibbles.make_deposit(1000).make_deposit(200).display_user_balance()
benny.make_deposit(7500).make_withdrawal(7500).make_withdrawal(4500).make_withdrawal(3000).display_user_balance()
nibbles.make_withdrawal(200).make_withdrawal(200).display_user_balance()
adrien.make_deposit(400).display_user_balance().transfer_money(benny, 400).display_user_balance()
benny.display_user_balance()
