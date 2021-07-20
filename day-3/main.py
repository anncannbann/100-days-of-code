
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



#leap year
'''
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



#Rolercoaster ticket counter
'''
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


'''
#pizza ordering
print('Welcome to Python Pizza 🍕 ')
print('********MENU********** \n Small Pizza: $15 \n Medium Pizza: $20 \n Large Pizza: $25 \n Pepperoni for Small Pizza: +$2 \n Pepperoni for Medium or Large Pizza: +$3 \n Extra cheese for any size pizza: + $1 \n')
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill =0
#size
if(size =='S'):
    bill = 15
elif(size =='M'):
    bill = 20
else:
    bill = 25

if(add_pepperoni =='Y'):
    if size =='S':
        bill+=2
    else:
        bill +=3

if(extra_cheese =='Y'):
    bill+=1

print(f'Your Bill is ${bill}')




'''

#Love Calculator

'''
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') +name2.count('u')
e = name1.count('e')+ name2.count('e')

l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')


true = t+r+u+e
love = l+o+v+e
score = int(str(true)+str(love))
if score < 10 or score >90:
    print(f'Your score is {score}, you go together like coke and mentos')
elif score > 40 and score <50:
    print(f'Your score is {score}, you are alright together.') 
else:
    print(f'Your score is {score}.')
'''
