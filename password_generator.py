# A Simple Password Generator
import random
from string import ascii_letters, digits, punctuation



# Version 1.0
"""List all viable characters for password then concatenate"""
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

all = lower + upper + numbers + symbols

length = 16

""" The 2nd parameter passed in to random.sample() can just be a number
it's just more readable with 'length' as the 2nd parameter"""
"""e.g. random.sample(all, 16)"""
password = "".join(random.sample(all, length))
print(password)



# Version 2.0
"""Import Python's built-in string classes then concatenate"""
# letters = ascii_letters
# numbers = digits
# punct = punctuation

# all = letters + numbers + punct

# length = 16

# password = "".join(random.sample(all, length))
# print(password)