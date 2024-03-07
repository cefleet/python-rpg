from Character import Character
from colorama import Fore
from menu import option_menu as menu
from color import prYellow

up = {"value":"w","title":"Move Up"}
left = {"value":"a", "title":"Move Left"}
down = {"value":"s", "title":"Move Down"}
right = {"value":"d", "title":"Move Right"}

class Player(Character):
    def __init__(self,name, power, hp, movement):
        super().__init__(name,power, hp, movement,2)
        self.symbol = '\xa5'
        self.color = Fore.BLACK

    def check_visiblity(self):
        for tile in self.map.d_map:
            if abs(self.location[0] - tile["location"][0]) + abs(self.location[1] - tile["location"][1]) <= self.vision:
                tile["visible"] = True
                tile["explored"] = True
            else:
                tile["visible"] = False

    def put_on_map(self, Map, location=[0,0]):
        super().put_on_map(Map, location)
        self.check_visiblity()
    
    def move(self, direction):
        super().move(direction)
        self.check_visiblity()
    
    def do_turn(self):
        # TODO make action options dependant on enemies
        prYellow("What would you like to do on your turn?")
        moves = []

        for tile in self.map.d_map:
            if [self.location[0]-1, self.location[1]] == tile["location"]:
                if tile["on"] == False and tile["wall"] == False:
                    moves.append(left)

            elif [self.location[0]+1, self.location[1]] == tile["location"]:
                if tile["on"] == False and tile["wall"] == False:
                    moves.append(right)

            elif [self.location[0], self.location[1]-1] == tile["location"]:
                if tile["on"] == False and tile["wall"] == False:
                    moves.append(up)
            
            elif [self.location[0], self.location[1]+1] == tile["location"]:
                if tile["on"] == False and tile["wall"] == False:
                    moves.append(down)

        action = menu(moves)
        self.move(action["value"])

