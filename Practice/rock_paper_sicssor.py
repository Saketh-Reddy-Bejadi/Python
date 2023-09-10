import random

def play_game(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

choices = ["rock", "paper", "scissors"]
player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
computer_choice = random.choice(choices)

if player_choice in choices:
    result = play_game(player_choice, computer_choice)
    print("Player's choice:", player_choice)
    print("Computer's choice:", computer_choice)
    print(result)
else:
    print("Invalid choice. Please choose from rock, paper, or scissors.")
