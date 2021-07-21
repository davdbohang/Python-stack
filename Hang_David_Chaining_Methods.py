class User:
    def __init__(self):
        self.name = "Michael"
        self.email = "michael@codingdojo.com"
        self.account_balance = 0

print("\n", "-"*100)

guido = User()
monty = User()

print(guido.name)
print(monty.email)

print("\n", "-"*100)

guido.name = "Guido"
monty.name = "Monty"

print(guido.name)
print(monty.name)

print("\n", "-"*100)

class User:
    def __init__(self, name, email_address):
        self.name = name
        self.email = email_address
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        return (f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, otherself, amount):
        self.account_balance -= amount
        otherself.account_balance += amount
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
steph = User("Stephen Curry", "steph@warriors.com")
print(guido.name)	# output: Guido van Rossum
print(monty.name)	# output: Monty Python
print(steph.name)

print("\n", "-"*100)

guido.make_deposit(100).make_deposit(200).make_deposit(200).make_withdrawal(50)

monty.make_deposit(200).make_deposit(150).make_withdrawal(100).make_withdrawal(75)

steph.make_deposit(1000).make_withdrawal(350).make_withdrawal(250).make_withdrawal(150)


print(guido.account_balance)	# output: 300
print(monty.account_balance)	# output: 50
print(steph.account_balance)

print("\n", "-"*100)

print(guido.display_user_balance())
print(monty.display_user_balance())
print(steph.display_user_balance())

print("\n", "-"*100)

print(guido.display_user_balance())
print(steph.display_user_balance())
guido.transfer_money(steph, 300)
print(guido.display_user_balance())
print(steph.display_user_balance())
