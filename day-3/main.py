
# odd-even
'''
n = int(input('Enter a number to check for even or odd?!'))
if(n %2==0):
    print('number is Even.')
else:
    print('Number is Odd.')
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
'''
#leap year
year = int(input('Enter a Year to Check:'))
if year % 4 == 0:
    if year % 100 ==0:
        if year % 400 ==0:
            print('It is a Leap Year!')
        else:
            print('It is NOT a leap Year')
    else:
        print('It is A Leap Year')
else:
    print('It is NOT a Leap Year')
'''


'''
#Rolercoaster ticket counter
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

bill =0
if height> 120:
    print('You are eligble for riding')
    age = int(input("Enter your Age to Continue"))
    if age >= 18:
        bill =12
        print(' Your ticket is $12')
    elif age >=12:
        bill =7
        print('Your ticket is $7')
    else:
        bill = 5
        print('Your ticket is $5')
    
    pix = input('Would you Like a Ticket? Y/N').lower()
    if(pix =='y'):
        bill+=3
    
    print(f'your Total is ${bill}')
else:
    print('Sorry you tiny, cant ride')
'''
