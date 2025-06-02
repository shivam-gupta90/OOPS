# - Create a class `BankAccount`
# - Attributes: account number, balance
# - Methods: `deposit()`, `withdraw()`, and `check_balance()`

class BankAccount:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance

    def Deposit(self,amount):
        self.balance += amount
        print("Rs",{amount},"is deposit") 
        print("total balance is :",self.balance)

    def Withdraw(self,amount):
        if amount <=self.balance:
           self.balance -= amount
           print("Rs",{amount},"was withdraw")
           print("total balance is :",self.balance)
        else:
            print("insuficent balance in account")

    def Check_balance(self):
        return self.balance           
acc1 =BankAccount("243211",4000)
print(acc1.Deposit(300))
print(acc1.Withdraw(200))