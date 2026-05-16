# ---------------------------------
# Typing Speed Test
# ---------------------------------

import time

print("===== TYPING SPEED TEST =====")

sentence = (
    "Python is a powerful programming language"
)

print("\nType This Sentence:")
print(sentence)

input("\nPress Enter When Ready...")

# Start Time
start_time = time.time()

# User Input
typed_text = input("\nStart Typing: ")

# End Time
end_time = time.time()

# Calculate Time
total_time = end_time - start_time

# Word Count
word_count = len(sentence.split())

# Words Per Minute
wpm = (word_count / total_time) * 60

print("\n===== RESULT =====")

# Check Accuracy
if typed_text == sentence:
    print("Accuracy: 100%")
else:
    print("Accuracy: Incorrect Typing")

print(f"Time Taken: {total_time:.2f} seconds")
print(f"Typing Speed: {wpm:.2f} WPM")
