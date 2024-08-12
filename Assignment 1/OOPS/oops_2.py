class Bank_Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance.")
    
    def get_balance(self):
        return self.balance

account = Bank_Account("123456789", "Kanchan", 20000)
account.deposit(500)
account.withdraw(200)
account.deposit(1000)
print(f"Current balance: {account.get_balance()}")
