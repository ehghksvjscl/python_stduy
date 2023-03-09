import random
from typing import List

OPTIONS: List = ["rock", "paper", "scissors"]

class RockPaperScissorsSimulator:
    def __init__(self):
        self.computer_choice = None
        self.human_choice = None
    def get_computer_choice(self):
        self.computer_choice = random.choice(OPTIONS)

    def get_human_choice(self):
        self.human_choice = OPTIONS[int(input("Enter your choice: ")) - 1]

    def print_options(self):
        print('\n'.join(f'({i}) {option.title()}' for i, option in enumerate(OPTIONS, 1)))

    def pirnt_choice(self, human_choice, computer_choice):
        print(f"You chose {human_choice}")
        print(f"Computer chose {computer_choice}")

    def print_win_lose(self, human_beats, human_loses_to):
        if computer_choice == human_loses_to:
            print(f"Sorry, computer: {self.computer_choice} you: {self.human_choice} lose!")
        elif computer_choice == human_beats:
            print(f"Oh, computer: {self.computer_choice} you: {self.human_choice} win")

    def print_result(self):
        if human_choice == computer_choice:
            print("Draw!")
        elif human_choice == 'rock':
            print_win_lose('rock', computer_choice, 'scissors', 'paper')
        elif human_choice == 'paper':
            print_win_lose('paper', computer_choice, 'rock', 'scissorsv')
        elif human_choice == 'scissors':
            print_win_lose('scissorsv', computer_choice, 'paper', 'rock')

    def run(self):
        self.print_options()
        self.get_human_choice()
        self.get_computer_choice()
        self.pirnt_choice()
        self.print_result()


RPS = RockPaperScissorsSimulator()
RPS.run()