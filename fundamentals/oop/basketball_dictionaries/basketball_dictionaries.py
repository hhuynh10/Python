class Player:
    def __init__(self, player):
        self.name = player['name']
        self.age = player['age']
        self.position = player['position']
        self.team = player['team']

    def __repr__(self):
        return f'Player: {self.name}, Age: {self.age}, Position: {self.position}, Team: {self.team}'

    @classmethod
    def get_team(cls, players):
        player_object = []
        for player in players:
            player_object.append(cls(player))
            return player_object

kevin = {
	"name": "Kevin Durant", 
	"age":34, 
	"position": "small forward", 
	"team": "Brooklyn Nets"
}
jason = {
	"name": "Jason Tatum", 
	"age":24, 
	"position": "small forward", 
	"team": "Boston Celtics"
}
kyrie = {
	"name": "Kyrie Irving", 
	"age":32, "position": "Point Guard", 
	"team": "Brooklyn Nets"
}
    
player_kevin = Player(kevin)
print(player_kevin)

player_jason = Player(jason)
print(player_jason.position)

player_kyrie = Player(kyrie)
print(player_kyrie.name)

players = [
    {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    },
    {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    },
    {
    "name": "Damian Lillard", 
    "age":33, "position": "Point Guard", 
    "team": "Portland Trailblazers"
    },
    {
    "name": "Joel Embiid", 
    "age":32, "position": "Power Foward", 
    "team": "Philidelphia 76ers"
    },
    {
    "name": "", 
    "age":16, 
	"position": "P", 
    "team": "en"
    }
]

new_team = []
for player in players:
    new_team.append(player)

print(new_team)
