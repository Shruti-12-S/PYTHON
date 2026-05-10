class BankAccount:
    def __init__(self,name,balance):
        self.name = name #public
        self.__balance = balance #private - data mangling

    def get_balance(self):#getter
        return self.__balance
    
    def set_balance(self, newBalance):#setter
        self.__balance = newBalance

acc1 = BankAccount("Shruti Shinde", 100000)
print(acc1.name, acc1._BankAccount__balance)
acc1.set_balance(200000)
print(acc1.name, acc1.get_balance())
