import random
from typeing import List

OPTIONS: List = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(OPTIONS)

def get_human_choice():
    return optins[int(input("Enter your choice: ")) - 1]

def print_options():
    print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(OPTIONS, 1)))

def pirnt_choice(human_choice, computer_choice):
    print(f"You chose {human_choice}")
    print(f"Computer chose {computer_choice}")

def print_win_lose(human_choice, computer_choice, human_beats, human_loses_to):
    if human_choice == human_loses_to:
        print(f"Sorry, computer: {computer_choice} you: {human_choice} lose!")
    elif computer_choice == human_beats:
        print(f"Oh, computer: {computer_choice} you: {human_choice} win")

def print_result(human_choice, computer_choice):
    if human_choice == computer_choice:
        print("Draw!")
    elif human_choice == 'rock':
        print_win_lose('rock', computer_choice, 'scissors', 'paper')
    elif human_choice == 'paper':
        print_win_lose('paper', computer_choice, 'rock', 'scissorsv')
    elif human_choice == 'scissors':
        print_win_lose('scissorsv', computer_choice, 'paper', 'rock')

print_options()
human_choice = get_human_choice()
computer_choice = get_computer_choice()
pirnt_choice(human_choice, computer_choice)
print_result(human_choice, computer_choice)