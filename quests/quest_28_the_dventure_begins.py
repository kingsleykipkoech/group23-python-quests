import random

options = ["rock", "paper", "scissors"]

player = input("Choose rock, paper, or scissors: ").strip().lower()

computer = random.choice(options)

print(f"\nYou chose: {player}")
print(f"Computer chose: {computer}\n")

if player == computer:
    print("It's a tie")

elif player == "rock" and computer == "scissors":
    print("Rock smashes scissors You win")
    
elif player == "paper" and computer == "rock":
    print("Paper covers rock  You win")
    
elif player == "scissors" and computer == "paper":
    print("Scissors cuts paper  You win")

else:
    
    print("You lose! The computer beat you.")
