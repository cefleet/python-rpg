from color import prRed, prYellow
from colorama import Fore, Style

class Character:
    def __init__(self,name, power, hp, movement, vision=2):
        self.name = name
        self.power = power
        self.hp = hp
        self.movement = movement
        self.map = False
        self.location = [0, 0]
        self.vision = vision
        self.symbol = 'C'
        self.color = Fore.RED

    def move(self, direction):
        if(self.map == False):
            return

        location = [False, False]

        if direction == "w":
            location = [self.location[0], self.location[1] - 1]
        elif direction == "d":
            location = [self.location[0]+1, self.location[1]]
        elif direction == "s":
            location = [self.location[0], self.location[1] + 1]
        elif direction == "a":
            location = [self.location[0]-1, self.location[1]]
        
        self.map.put_character_on_location(self,location)

    def put_on_location(self, location):
        self.location = location

    def put_on_map(self, Map, location):
        self.map = Map
        self.map.put_character_on_location(self, location)
    
    def attack(self, target):
        target.take_damage(self.power)

    def take_damage(self, amount):
        self.hp -= amount
        prYellow(self.name + ' has taken '+ str(amount)+' damage.')
        if self.hp <= 0:
            self.dead = True
            prRed(self.name + ' has died.')
    
    def __str__(self):
        string = Fore.YELLOW + '~~~~~~ ' + str(self.name) + ' ~~~~~~'+ Style.RESET_ALL + '\n'
        string += 'Power : ' + Fore.RED + str(self.power) + Style.RESET_ALL + '\n'
        string += 'HP : ' + Fore.GREEN +  str(self.hp) + Style.RESET_ALL + '\n'
        string += 'Movement : ' + Fore.BLUE + str(self.movement) + Style.RESET_ALL + '\n'
        return string

            