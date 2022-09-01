class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        
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


user1 = User('Hung', 'Huynh', 'hungpchuynh@gmail.com', 30)

user1.display_info()

user1.enroll()
print(user1.is_rewards_member)
print(user1.gold_card_points)

user1.spend_points(300)
print(user1.gold_card_points)