from colorama import init, Back, Style
init()
from Player import Player
from menu import option_menu as menu
from color import prYellow
from Map import Map
from clear_screen import clear_screen

from level1 import level1

player = False

player_classes = [{
    "c_class":"Rogue",
    "power":4,
    "hp":12,
    "movement":3
},{
    "c_class":"Barbarian",
    "power":5,
    "hp":15,
    "movement":2
},{
    "c_class":"Knight",
    "power":2,
    "hp":20,
    "movement":1
}]

player_class_options = [{"value":1, "title":"Rouge"}, {"value":2, "title":"Barbarian"}, {"value":3,"title":"Knight"}]
dungon_map = Map(level1)

def main():
    global player
    prYellow('Enter your characters name:')
    player_name = input('')
    clear_screen()

    prYellow("Select Character Class:")
    player_class_option = menu(player_class_options)
    player_class = player_classes[player_class_option["value"]-1]
    player = Player(player_name + ' The '+player_class['c_class'], player_class["power"], player_class["hp"], player_class["movement"])
    
    player.put_on_map(dungon_map,[0,0])

    while True:
        clear_screen()
        draw_screen()
        player.do_turn()
        


def draw_screen():
    print(player)
    
    dungon_map.print_map()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('\ngoodby')
        pass