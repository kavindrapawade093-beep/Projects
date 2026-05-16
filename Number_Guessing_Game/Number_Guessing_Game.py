# ---------------------------------
# Number Guessing Game
# ---------------------------------

import random

print("===== NUMBER GUESSING GAME =====")

# Random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

while True:

    guess = int(input("Guess the Number (1-100): "))

    attempts += 1

    # Correct Guess
    if guess == secret_number:
        print("\n🎉 Congratulations!")
        print("You guessed the correct number.")
        print("Attempts:", attempts)
        break

    # Hint
    elif guess < secret_number:
        print("Too Low! Try Again.")

    else:
        print("Too High! Try Again.")

print("Game Over!")
