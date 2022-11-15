import rich

def correct_place(letter):
    return f'[black on green]{letter}[/]'

def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'

def incorrect(letter):
    return f'[black on white]{letter}[/]'

WELCOME_MESSAGE = correct_place("WELCOME") + " " + incorrect("TO") + " " + correct_letter("TWORDLE") + "\n"

def main():
    rich.print(WELCOME_MESSAGE)

if __name__ == '__main__':
    main()