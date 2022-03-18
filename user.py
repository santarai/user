class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount):
        self.amount += amount

    def make_withdrawl(self,amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


Dorje = User("Dorje")
Dawa = User("Mr. Dawa")
Nima = User("Nima")

Dorje.make_deposit(100)
Dorje.make_deposit(200)
Dorje.make_deposit(50)
Dorje.make_withdrawl(45)
Dorje.display_user_balance()

Dawa.make_deposit(1000)
Dawa.make_deposit(1000)
Dawa.make_withdrawl(500)
Dawa.make_withdrawl(300)
Dawa.display_user_balance()

Nima.make_deposit(1500)
Nima.make_withdrawl(1000)
Nima.make_withdrawl(5000)
Nima.make_withdrawl(3000)
Nima.display_user_balance()


Dawa.transfer_money(400, Dorje) 