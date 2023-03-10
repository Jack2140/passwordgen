import string
import secrets

letters = string.ascii_letters
numbers = string.digits
special_char = string.punctuation

character = letters

if numbers:
    character += numbers
if special_char:
    character += special_char

password = ""
length = int(input("Enter the length: "))
counter = 0

while counter < length:
    count_pass = secrets.choice(character)
    password += count_pass
    counter += 1
print("Your Password is:" , password)

