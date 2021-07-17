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
print(type(n))

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


#Coding Challenge = Life in Weeks.