from color import prRed, prCyan, prYellow

def option_menu(options):
    answer = False
    value = False

    while True:
        for option in options:
            prYellow(str(option["value"])+'. '+option["title"])
    
        prCyan("Enter value from list above:")
        answer = input('')
        try:
            answer = str(answer)
            for option in options:
                if str(option['value']) == answer:
                    value = option
            if value != False:
                break
            else:
                raise
        except:
            prRed(str(answer) + ' Is an invalid value.')
    return value