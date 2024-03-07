from Character import Character
import random

class Monster(Character):
    def __init__(self,name, power, hp, movement):
        super().__init__(name,power, hp, movement)

    def move():
        direction = random.randint(1, 4)
        super().move(direction)
    