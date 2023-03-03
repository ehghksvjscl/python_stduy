import random

optins = ["rock", "paper", "scissors"]
print("(1) Rock\n(2) Paper\n(3) Scissors")
human_coice = optins[int(input("Enter your choice: ")) - 1]
print(f"You chose {human_coice}")
computer_choice = random.choice(optins)
print(f"Computer chose {computer_choice}")
if human_coice == "rock":
    if computer_choice == "paper":
        print("Sorry, you lose!")
    elif computer_choice == "scissors":
        print("You win!")
    else:
        print("Draw!")
elif human_coice == "paper":
    if computer_choice == "scissors":
        print("Sorry, you lose!")
    elif computer_choice == "rock":
        print("You win!")
    else:
        print("Draw!")
elif human_coice == "scissors":
    if computer_choice == "rock":
        print("Sorry, you lose!")
    elif computer_choice == "paper":
        print("You win!")
    else:
        print("Draw!")
