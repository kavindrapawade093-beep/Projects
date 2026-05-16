# ---------------------------------
# Quiz Game Project
# ---------------------------------

print("===== PYTHON QUIZ GAME =====")

score = 0

# Question 1
answer = input("\n1. What is the capital of India? ")

if answer.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer")

# Question 2
answer = input("\n2. Which language is used for AI and ML? ")

if answer.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer")

# Question 3
answer = input("\n3. What does CPU stand for? ")

if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer")

# Question 4
answer = input("\n4. Which planet is known as the Red Planet? ")

if answer.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer")

# Question 5
answer = input("\n5. What is the full form of HTML? ")

if answer.lower() == "hyper text markup language":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer")

# Question 6
answer = input("\n6. Which company created Python? ")

if answer.lower() == "google":
    print("Wrong Answer")
else:
    print("Correct!")
    score += 1

# Question 7
answer = input("\n7. Which keyword is used to create a function in Python? ")

if answer.lower() == "def":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer")

# Question 8
answer = input("\n8. What is 10 + 20? ")

if answer == "30":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer")

# Question 9
answer = input("\n9. Which data type stores True or False values? ")

if answer.lower() == "boolean":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer")

# Question 10
answer = input("\n10. Which symbol is used for comments in Python? ")

if answer == "#":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer")

# Question 11
answer = input(
    "\n11. Which loop is used when the number of iterations is unknown? ")

if answer.lower() == "while":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer")

# Question 12
answer = input("\n12. Which operator is used for multiplication in Python? ")

if answer == "*":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer")

# Question 13
answer = input("\n13. What is the extension of Python files? ")

if answer.lower() == ".py":
    print("Correct!")
    score += 1
else:
    print("Wrong Answer")

# Final Score
print("\n===== QUIZ COMPLETED =====")
print("Your Score:", score, "/ 13")

# Result
if score >= 11:
    print("Excellent!")
elif score >= 7:
    print("Good Job!")
else:
    print("Keep Practicing!")

print("\n===== THANKS FOR PLAYING =====")

# ---------------------------------
# Quiz Game Project
# ---------------------------------
