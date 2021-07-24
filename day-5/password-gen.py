#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password=''


for i in range(0,nr_letters):
    #password+=str(random.choices(letters))
    x = random.randint(0,nr_letters-1)
    password+= letters[x]

for i in range(0,nr_symbols):
    x = random.randint(0,nr_symbols-1)
    password+= symbols[x]

for i in range(0,nr_numbers):
    x = random.randint(0,nr_numbers-1)
    password+= numbers[x]

print(f'Your Easy  Password is {password}')
 
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


new_p = random.sample(password , len(password))
new_password = ''.join(new_p)
print(f'Your Hard  Password is {new_password}')

