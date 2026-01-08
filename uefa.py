import random

class Team:
    def __init__(self, name, nat, num):
        self.name = name
        self.nat = nat
        self.num = num

teams = [
    Team("PSG", "France", 2),
    Team("Liverpool", "England", 1),
    Team("Inter", "Italy", 1),
    Team("Manchester City", "England", 1),
    Team("Leipzig", "Germany", 2),
    Team("Eintracht Frankfurt", "Germany", 2),
    Team("Napoli", "Italy", 1),
    Team("Porto", "Portugal", 2),
    Team("Club Brugge", "Belgium", 2),
    Team("Benfica", "Portugal", 1),
    Team("Tottenham", "England", 2),
    Team("Milan", "Italy", 1),
    Team("Bayern", "Germany", 1),
    Team("Real Madrid", "Spain", 2),
    Team("Chelsea", "England", 2),
    Team("Dortmund", "Germany", 1)
]

first_place = []
second_place = []

for team in teams:
    if(team.num == 1):
        first_place.append(team)
    else:
        second_place.append(team)

def valid(opp1, opp2):
    if opp1.nat == opp2.nat:
        return False
    
    if (opp1.nat == "Ukraine" and opp2.nat == "Russia") or (opp2.nat == "Ukraine" and opp1.nat == "Russia"):
        return False
    
    return True

matches = []
while first_place:
    opp1 = random.choice(first_place)
    while True:
        opp2 = random.choice(second_place)
        if valid(opp1, opp2): break
    matches.append((opp1, opp2))
    first_place.remove(opp1)
    second_place.remove(opp2)


for match in matches:
    print(f'{match[0].name} vs {match[1].name}')