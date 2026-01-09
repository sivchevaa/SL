class Animal:
    def __init__(self, type, talk):
        self.type = type
        self.talk = talk

    def Talk(self):
        print(f"{self.talk}")
        return None

cat = Animal('cat', 'Meow')
dog = Animal('dog', 'Woof Woof')
mous = Animal('mous', 'Tsur')
wolf = Animal('wolf', 'Aaauuuuuu')
horse = Animal('horse', 'Ppfffff')

while True:
    species = str(input("Animal: ")).lower()
    if species == 'cat':
        cat.Talk()
    elif species == 'dog':
        dog.Talk()
    elif species == 'mous':
        mous.Talk()
    elif species == 'wolf':
        wolf.Talk()
    elif species == 'horse':
        horse.Talk()
    elif species == 'end':
        break
    else:
        print("No such animal.")