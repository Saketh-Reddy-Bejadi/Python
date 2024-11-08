import random

def play_game(pc, cc):
    if pc == cc:
        return "It's a tie!"
    elif (
        (pc == "rock" and cc == "scissors") or
        (pc == "paper" and cc == "rock") or
        (pc == "scissors" and cc == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

c = ["rock", "paper", "scissors"]
pc = input("Enter your choice (rock, paper, scissors): ").lower()
cc = random.choice(c)

if pc in c:
    r = play_game(pc, cc)
    print("Player's choice:", pc)
    print("Computer's choice:", cc)
    print(r)
else:
    print("Invalid choice. Please choose from rock, paper, or scissors.")
