# ---------------------------------
# Rock Paper Scissors Game
# ---------------------------------

import random

print("===== ROCK PAPER SCISSORS =====")

options = ["rock", "paper", "scissors"]

while True:

    # User Choice
    user_choice = input(
        "\nEnter Rock, Paper, or Scissors: "
    ).lower()

    # Check Input
    if user_choice not in options:
        print("Invalid Choice")
        continue

    # Computer Choice
    computer_choice = random.choice(options)

    print("Computer Chose:", computer_choice)

    # Draw
    if user_choice == computer_choice:
        print("It's a Draw!")

    # User Wins
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You Win!")

    # Computer Wins
    else:
        print("💻 Computer Wins!")

    # Play Again
    again = input("\nPlay Again? (yes/no): ").lower()

    if again != "yes":
        print("Game Closed")
        break
