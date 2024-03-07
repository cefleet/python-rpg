from colorama import Back, Style

class Map:
    def __init__(self,d_map):
        self.d_map = d_map
    
    def put_character_on_location(self,character,location):

        for tile in self.d_map:
            if(tile["location"] == character.location):
                tile["on"] = False

        for tile in self.d_map:
            if tile["location"] == location:
                character.put_on_location(location)
                tile["on"] = character

    def print_map(self):
        on_row = 0
        output = ''
        for tile in self.d_map:
            if on_row != tile["location"][1]:
                output += '\n'
                on_row += 1
            middle = ' '

            if tile["on"] != False:
                middle = tile["on"].color + tile["on"].symbol

            if tile["visible"] != True and tile["explored"] != True:
                output += Back.BLACK + '   ' + Style.RESET_ALL
                continue
            if tile["wall"] == True:
                if tile["visible"] == True:
                    output += Back.LIGHTBLUE_EX + '   ' + Style.RESET_ALL
                else:
                    output +=  Back.BLUE + '   ' + Style.RESET_ALL
            else:
                if tile["visible"] == True:
                    output += Back.LIGHTGREEN_EX + ' ' + middle + ' ' + Style.RESET_ALL
                else:
                    output += Back.GREEN + ' ' + middle + ' ' + Style.RESET_ALL
        print(output)