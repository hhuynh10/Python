class BankAccount:

    accounts = []

    def __init__(self, int_rate = 0.01, balance= 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Balance: {self.balance}")
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Balance: {self.balance}")
            return self
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - amount - 5
            print(self.balance)
            return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance >= 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            print(f"Balance: {self.balance}")
            return self
    
    @classmethod
    def print_balances(cls):
        for account in cls.accounts:
            account.display_account_info()

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.account = {
            "Checking" : BankAccount(.1, 100),
            "Saving" : BankAccount(.25, 5000)
        }
        
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f'First Name = {self.first_name}')
        print(f'Last Name = {self.last_name}')
        print(f'Email = {self.email}')
        print(f'Age = {self.age}')

    def enroll(self):
        if self.is_rewards_member == True:
            print('User already a member.')
            self.gold_card_points = 0
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        if amount <= self.gold_card_points:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print('Not enough gold')
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance (self):
        self.account.display_account_info()
        print(self.account.display_account_info)
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self

user1 = User('Hung', 'Huynh', 'hungpchuynh@gmail.com', 30)
user1.account["Checking"].deposit(300).withdraw(600).display_account_info()
user1.account["Saving"].deposit(500).display_account_info()