import random

class Hat:
    house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.house))

hat = Hat()
hat.sort("Harry")