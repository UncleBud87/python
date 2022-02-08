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

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name} ,Balence {self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance = self.account_balance - amount
        other_user.account_balance = other_user.account_balance + amount


adrien = User("Adrien", "adrien@python.com")
nibbles = User("Mr. Nibbles", "nibbles@python.com")
benny = User("Benny Bob", "bennybob@python.com")

adrien.make_deposit(105)
adrien.make_deposit(100)
adrien.make_deposit(100)
adrien.display_user_balance()

nibbles.make_deposit(1000)
nibbles.make_deposit(200)
nibbles.display_user_balance()

benny.make_deposit(7500)
benny.make_withdrawal(7500)
benny.make_withdrawal(4500)
benny.make_withdrawal(3000)
benny.display_user_balance()

nibbles.make_withdrawal(200)
nibbles.make_withdrawal(200)
nibbles.display_user_balance()

adrien.make_deposit(400)
adrien.display_user_balance()
adrien.transfer_money(benny, 400)
adrien.display_user_balance()

#benny.display_user_balance()
