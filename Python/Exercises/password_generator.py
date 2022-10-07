# Step 1: Import necessary modules

import secrets
import string

# Step 2: Define the alphabet

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation
alphabet = letters + digits + special_chars

# Step 3: Fix the length of the password; Generate a password

pwd_length = 5
pwd = ''
for i in range(pwd_length):
  pwd += ''.join(secrets.choice(alphabet))

print(pwd)