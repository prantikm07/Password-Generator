#Password Generator Project
import random

letters = []
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '_', '@', '*', '+']

for i in range(97, 123):   # lowercase letters
    letters.append(chr(i))

for i in range(65, 91):    # uppercase letters
    letters.append(chr(i))


print("Welcome to the PyPassword Generator!...")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

passlist = []
for i in range(0, nr_letters):
    passlist.append(random.choice(letters))

for i in range(0, nr_symbols):
    passlist.append(random.choice(symbols))

for i in range(0, nr_numbers):
    passlist.append(random.choice(numbers))

# Shuffle the list to randomize the password
random.shuffle(passlist)

password = ""

for char in passlist:
    password += char

print("Your genarated password is: " + password)