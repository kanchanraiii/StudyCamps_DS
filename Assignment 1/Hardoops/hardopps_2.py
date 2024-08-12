class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance is {self.balance}."

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}."
        else:
            return "Insufficient balance."

class SavingsAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied. New balance is {self.balance}."

class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, overdraft_limit=500):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrew {amount}. New balance is {self.balance}."
        else:
            return "Overdraft limit exceeded."

class Bank:
    def __init__(self):
        self.accounts = []

    def create_savings_account(self, account_number, balance=0, interest_rate=0.02):
        account = SavingsAccount(account_number, balance, interest_rate)
        self.accounts.append(account)
        return f"Savings account {account_number} created."

    def create_checking_account(self, account_number, balance=0, overdraft_limit=500):
        account = CheckingAccount(account_number, balance, overdraft_limit)
        self.accounts.append(account)
        return f"Checking account {account_number} created."

    def transfer_money(self, from_account_number, to_account_number, amount):
        from_account = next((acc for acc in self.accounts if acc.account_number == from_account_number), None)
        to_account = next((acc for acc in self.accounts if acc.account_number == to_account_number), None)
        if from_account and to_account:
            withdraw_msg = from_account.withdraw(amount)
            if "Withdrew" in withdraw_msg:
                to_account.deposit(amount)
                return f"Transferred {amount} from {from_account_number} to {to_account_number}."
            else:
                return withdraw_msg
        else:
            return "Account not found."

    def generate_statement(self, account_number):
        account = next((acc for acc in self.accounts if acc.account_number == account_number), None)
        if account:
            return f"Account {account_number} Statement: Balance = {account.balance}"
        else:
            return "Account not found."
        
bank = Bank()
print(bank.create_savings_account("S001", 1000))
print(bank.create_checking_account("C001", 500))
savings_account = next(acc for acc in bank.accounts if acc.account_number == "S001")
print(savings_account.deposit(500))
print(savings_account.withdraw(200))
print(savings_account.apply_interest())
print(bank.transfer_money("S001", "C001", 300))
print(bank.generate_statement("S001"))
print(bank.generate_statement("C001"))
