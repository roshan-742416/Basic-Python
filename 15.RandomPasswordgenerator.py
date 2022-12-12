# Random password generator
# Password Generator Example

# Import relevant modules
import random

# Import special characters i.e. punctuation
from string import punctuation

# Create a list with all the special characters

special_characters = list(punctuation)
# There are 32 characters in the list

# Example random password generator with special characters

password = ""
for i in range(5):
    a = chr(random.randint(65, 90)) #Produces random uppercase letter
    b = chr(random.randint(65, 90)).lower() # Produces random lowercase letter
    c = special_characters[random.randint(0, 31)]
    d = str(random.randint(0, 9))
    password = password + a + b + c + d
# Shuffle string of password, so that it doesn't follow
# Uppercase, lowercase, special character structure and number
''.join(random.sample(password, len(password)))
print(password)
