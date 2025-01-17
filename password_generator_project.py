#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) #user enters value
nr_symbols = int(input(f"How many symbols would you like?\n")) #user enters value
nr_numbers = int(input(f"How many numbers would you like?\n")) #user enters value


password = [] #an empty list to store the password
for letter in range(0,nr_letters): #loop through the range of o to user input
    #picks a random choice of letters in the range above and adds it to password list
    password += random.choice(letters) 
for symbol in range(0,nr_symbols):
    password += random.choice(symbols)
for number in range(0,nr_numbers):
    password += random.choice(numbers)
random.shuffle(password)
print('Your password is:',''.join(password))