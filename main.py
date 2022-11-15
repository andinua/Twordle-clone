import rich
from rich.prompt import Prompt
from rich.console import Console

def correct_place(letter):
    return f'[black on green]{letter}[/]'

def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'

def incorrect(letter):
    return f'[black on white]{letter}[/]'

WELCOME_MESSAGE = correct_place("WELCOME") + " " + incorrect("TO") + " " + correct_letter("TWORDLE") + "\n"

def score_guess(guess, answer):
    scored = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            scored += correct_place(letter)
        elif letter in answer:
            scored += correct_letter(letter)
        else:
            scored += incorrect(letter)
    return ''.join(scored)

def main():
    rich.print(WELCOME_MESSAGE)

    allowed_guesses = 6
    used_guesses = 0

    console = Console()
    answer_word = Prompt.ask("Enter a word")
    console.clear()

    while used_guesses < allowed_guesses:
        used_guesses += 1
        guess = Prompt.ask("Enter your guess")
        console.print(score_guess(guess, answer_word))
        if guess == answer_word:
            break
    print(f"\n\nTWORDLE {used_guesses}/{allowed_guesses}\n")

if __name__ == '__main__':
    main()