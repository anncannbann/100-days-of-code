
# odd-even
'''
n = int(input('Enter a number to check for even or odd?!'))
if(n %2==0):
    print('number is Even.')
else:
    print('Number is Odd.')
'''

#Rolercoaster ticket counter
'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height> 120:
    print('You are eligble for riding')
    age = int(input("Enter your Age to Continue"))
    if age >= 18:
        print(' Your total is $12')
    elif age >=12 and age< 18:
        print('Your total is $7')
    else:
        print('Your total is $5')
else:
    print('Sorry you tiny, cant ride')

'''

#BMI 2.0
'''
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


h1 = float(height)
w1 = float(weight)

bmi = round(w1 / (h1 **2))

if(bmi <18.5):
    print(f'your BMI is ${bmi} , you are underweight')
elif(bmi >18.5 and bmi< 25):
    print(f'Your BMI is {bmi} andf you have a normal weight')
elif(bmi > 25 and bmi <30):
    print(f'Your BMI is {bmi}, you are slightly overrweight')
elif(bmi > 30 and bmi <35):
      print(f'Your BMI is {bmi}, you are Obese')
else:
      print(f'Your BMI is {bmi}, you are Clinically Obese.')
    '''

#leap year
