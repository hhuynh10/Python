class BankAccount:
    all_account = []
    def __init__(self, interest, balance):
        self.interest = interest
        self.balance = balance
        BankAccount.all_account.append(self)
    

    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        return self

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            print(self.balance)
        if (self.balance - amount) < 0:
            print('Insufficient fund')
            self.balance -= 5
        return self

    def display(self):
        print(f"Balance: ${self.balance}")

    def yeild_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.interest)
            print(self.balance)
        return self

    @classmethod
    def all_balance(cls):
        for account in cls.all_account:
            account.display()


user1 = BankAccount(0.1, 200)

user2 = BankAccount(0.3, 100)

user1.deposit(300).deposit(100).deposit(50).withdraw(100).yeild_interest().display()
user2.deposit(600).deposit(200).withdraw(50).withdraw(100).withdraw(30).withdraw(800).yeild_interest().display()

BankAccount.all_balance()