#Create a class BankAccount with private attributes account_number and balance. Provide methods to deposit, withdraw, and check balance.

class BankAccount:

    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance

    def deposit(self,x):
        self.__balance=x+self.__balance
        print(f"Deposit of {x} sucessfull, your current Balance is {self.__balance}")

    def withdraw(self,y):
        self.__balance=self.__balance-y
        print(f"withdraw of {y} is sucessfull,your current Balance is {self.__balance} ")

    def Balance(self):
        print(f"Your current balance is {self.__balance}")

person1=BankAccount("12341234",5000)
#person1.Balance()
#person1.deposit(2000)
person1.withdraw(2000)
