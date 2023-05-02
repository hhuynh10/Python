class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

        BankAccount.all_accounts.append(self)
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance < amount:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(self.balance)
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
        return self
    
    @classmethod
    def account_balances(cls):
        for account in cls.all_accounts:
            account.display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {
                        "account1" : BankAccount(int_rate=0.02, balance=100),
                        "account2" : BankAccount(int_rate=0.02, balance=150)
                        }

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawal (self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        self.account.display_account_info()

user1 = User("Hayden", "hayden@gmail.com")

user1.account["account1"].deposit(100).display_account_info()
