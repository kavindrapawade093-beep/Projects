# ---------------------------------
# Password Generator Project
# ---------------------------------

import random
import string

print("===== PASSWORD GENERATOR =====")

# Password Length
length = int(input("Enter Password Length: "))

# Characters Used
characters = (
    string.ascii_letters +
    string.digits +
    string.punctuation
)

# Generate Password
password = ""

for i in range(length):
    password += random.choice(characters)

# Output
print("\nGenerated Password:")
print(password)
