# Challange 4
class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate

title = input("Enter the account title: ")
balance = int(input("Enter the account balance: "))

account = Account(title, balance)

interestRate = float(input("Enter the interest rate: "))

savings_account = SavingsAccount(title, balance, interestRate)

print("Account details are: ")
print("Title:", account.title)
print("Balance:", account.balance)

print("Saving_account details are: ")
print("Title:", savings_account.title)
print("Balance:", savings_account.balance)
print("Interest Rate:", savings_account.interestRate)