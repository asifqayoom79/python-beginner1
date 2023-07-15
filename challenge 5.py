# Challange 5
class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

    def getBalance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance!")

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

    def interestAmount(self):
        return self.balance * (self.interestRate / 100)


title = input("Enter account title: ")
balance = float(input("Enter account balance: "))
interestRate = float(input("Enter interest rate (%): "))

account = Account(title, balance)
savings_account = SavingsAccount(title, balance, interestRate)

amount = float(input("Enter deposit amount: "))
account.deposit(amount)
print("Updated Account Balance after deposit:",account.getBalance())

amount = float(input("Enter withdrawal amount: "))
account.withdrawal(amount)
print("Updated Account Balance after withdrawal:",account.getBalance())

interest_amount = savings_account.interestAmount()
print("Savings Account Interest Amount:",interest_amount)