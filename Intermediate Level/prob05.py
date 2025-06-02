# - Create a class `Account` and `SavingsAccount` that inherits from it
# - Add interest rate to `SavingsAccount`
# - Override the withdrawal method with interest deduction logic

class Account:
    def __init__(self,acc_no,balance):
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}") 

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def __str__(self):
        return f"Account({self.account_number}) - Holder: {self.holder_name}, Balance: {self.balance}"
    

class Savingaccount(Account):
    def __init__(self,acc_no,balance,interset_rate):
        super().__init__(acc_no,balance,)
        self.interset_rate = interset_rate
        
    def withdraw(self,amount):
        interset = (amount * self.interset_rate) / 100
        total_deduction = amount + interset   
        if total_deduction >= self.balance:
            print("Insuficent balance after include interset")
        else:
            self.balance -= total_deduction
            print(f"withdaw {amount} + {interset} (interest). New balance: {self.balance}")    

acc = Savingaccount(2432,1000, 5)

acc.deposit(500)
acc.withdraw(400)