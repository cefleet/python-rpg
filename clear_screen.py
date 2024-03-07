def clear_screen():
    LINE_UP = '\033[1A'
    LINE_CLEAR = '\x1b[2K'
    for i in range(100):
        print(LINE_UP, end=LINE_CLEAR)
