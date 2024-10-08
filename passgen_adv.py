# Enhanced Password Generator Project
import random
import string

# Lists for different character types
letters = string.ascii_letters  # Both uppercase and lowercase
numbers = string.digits
symbols = "!#$%&@_*+"

print("Welcome to the PyPassword Generator!")


nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

complexity = input("Choose a complexity level (low, medium, high):\n").lower()
save_option = input("Would you like to save the generated password to a file? (yes/no):\n").lower()

# Password character list
passlist = []
for _ in range(nr_letters):
    passlist.append(random.choice(letters))

for _ in range(nr_symbols):
    passlist.append(random.choice(symbols))

for _ in range(nr_numbers):
    passlist.append(random.choice(numbers))

# Shuffle the list to randomize the password
random.shuffle(passlist)
password = "".join(passlist)

# Enhance password based on complexity
if complexity == "medium":
    password += random.choice(symbols) + random.choice(numbers)
elif complexity == "high":
    for _ in range(3):  # Add more random elements for high complexity
        password += random.choice(letters + symbols + numbers)

# Display the password
print("Your generated password is:", password)

# Save password to a file if the user opts in
if save_option == "yes":
    with open("generated_password.txt", "a") as file:
        file.write(f"Generated password: {password}\n")
    print("Password saved to 'generated_password.txt'.")

# Final output with complexity details
print(f"Password complexity: {complexity.capitalize()}")
