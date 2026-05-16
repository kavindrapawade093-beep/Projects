# ---------------------------------
# URL Shortener Project
# ---------------------------------

import pyshorteners

print("===== URL SHORTENER =====")

# Long URL
long_url = input("Enter Long URL: ")

# Create Shortener
shortener = pyshorteners.Shortener()

# Short URL
short_url = shortener.tinyurl.short(long_url)

print("\nShort URL:")
print(short_url)

print("\nLong URL:")
print(long_url)
