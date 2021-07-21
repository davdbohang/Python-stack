class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds: Charging a $5 Fee")
            self.balance -= 5
            return self
        else: 
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"{self.name}'s Balance: ${self.balance}")


    def yield_interest(self):
        if self.balance > 0:
            self.balance *= self.int_rate
        return self

# klay = BankAccount("Klay Thompson", .01, 0)
# steph = BankAccount("Steph Curry", .01, 0)

# print("\n", "-"*100)

# print(steph.name)
# print(klay.name)

# print("\n", "-"*100)

# steph.deposit(1000).deposit(200).deposit(300).withdraw(550)
# klay.deposit(2000).deposit(200).withdraw(300).withdraw(150).withdraw(250)

# # print(steph.account_balance)
# # print(klay.account_balance)

# steph.display_account_info()
# klay.display_account_info()

class User:
    def __init__(self, username, email, account):
        self.username = username
        self.email = email
        self.account = [BankAccount(int_rate=0.02, balance=0)]

    def make_deposit(self, accnum, amount):
        self.account[accnum].balance += amount
    # def make_deposit_savings(self, amount):
    #     self.account_savings.balance += amount

    def make_withdrawal(self, accnum, amount):
        self.account[accnum].balance -= amount
    # def make_withdrawal_savings(self, amount):
    #     self.account_savings.balance -= amount

    def display_user_balance(self, accnum):
        print (f"User {self.username}, Account Balance: ${self.account[accnum].balance}")
    
    def transfer_from_savings(self, amount):
        if self.account_savings.balances < amount:
            return "user has insufficient funds!"
        else:
            self.account_savings.balance -= amount
            self.account.balance += amount
    def transfer_from_checking(self, amount):
        if self.account.balance < amount:
            return "user has insufficient funds!"
        else:
            self.account.balance -= amount
            self.account_savings.balance += amount

    def add_account(self):
        self.account.append(BankAccount(0,0))

stephen = User("Stephen Curry", "stephen@warriors.com", 0) # creating inital account account[0]
klay = User("Klay", "klay@warriors.com", 0)

print("\n", "-"*30,"Deposit $1000 to Checking", "-" * 30)

stephen.add_account() # creating second account account[1]
stephen.make_deposit(0, 1000)
print(stephen.account[0].balance)
stephen.make_deposit(1, 100000)
print(stephen.account[1].balance)

stephen.make_deposit(0, 10000)
stephen.display_user_balance(0)
stephen.display_user_balance(1)


print("\n", "-"*30,"Transfer $500 to Savings", "-"*30)

# stephen.transfer_from_checking(500)
# stephen.display_user_balance()

# stephen.add_account()
# print(stephen.bankaccount[0])
# print(stephen.account[0])