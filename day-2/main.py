#----------------Data types-------------
'''
#subscripting.....
print("Hello"[4])

#int
print(123 +345)

# we can write 123,234,234 as 
print(123_234_234)


#float
3.14159

#Boolean
True
False

'''

'''
# Type-Check, Type -Errors and Type Conversion

n= len(input('Whats is your name?'))
#print('Your name has ' + n+ 'letters lol')
print('Your name has ' + str(n)+ 'letters lol')

#how to see type
print(type(n
))

#type conversion / type casting.
x = str(n)
print(type(x))

'''

'''
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

x = input("Type a Two Digit Number: ")
print(type(x))
print(int(x[0])+ int(x[1]))


#MATHEMATICAL OPERATIONS

print(type(6/3))
print(type(6**4))

print(3*3+3/3-3)

'''

'''
#BMI CALCULATOR
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


h1 = float(height)
w1 = float(weight)

bmi = w1 / (h1 **2)
print(int(bmi))
'''

#Number Manipulation


# print(round(8/3,9))
# print(8/3)

'''
score = 0
height = 1.8
winning = True
#f-string
print(f'Your score is : {score} and height is {height} and you won {winning}')
'''

'''
#Coding Challenge = Life in Weeks.
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# Where x, y and z are replaced with the actual calculated numbers.

age = int(input('Enter your Age :'))
expected_age = 90
days = (expected_age - age) *365
weeks = (expected_age - age) *52
months = (expected_age - age) *12
print(f'You have {days} days , {weeks} weeks and {months} months')
'''



#Bill Calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
print('Welcome to the Bill Calculator!!')
bill = float(input("Enter your Bill Amount :"))
n = int(input('Enter the Number of People:'))
tip = int(input('Enter the tip amount 10 or 12 or 15'))

total = (bill * (tip /100) + bill ) / n
t_format = "{:.2f}".format(total)
# print(f'Each person has to pay {round(total,2)}')
print(f'Each person has to pay {t_format}')

