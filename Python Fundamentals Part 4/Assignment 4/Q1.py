'''
Concept: Classes & Objects
Create a BankAccount class with attributes account_number, owner_name, and balance.
Add methods to deposit, withdraw and check balance.
'''

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,moneyAdd):
        self.balance+=moneyAdd
        print(f"Rs. {moneyAdd} deposited successfully")
        print(f"Current Balance: Rs.{self.balance}")

    def withdraw(self, moneySub):
        if moneySub > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= moneySub
            print(f"₹{moneySub} withdrawn successfully")
            print(f"Remaining Balance: ₹{self.balance}")

    def check_balance(self):
            print(f"Current Balance: ₹{self.balance}")

acc = BankAccount(101,"Shruti",5000)

acc.deposit(1000)
acc.withdraw(200)
acc.check_balance()