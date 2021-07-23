import random

rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)

      (____)
---.__(___)
'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game = [rock,paper,scissors]

computer = random.choice(game)
user = input('Enter your choice.\n 0 for Rock, 1 for Paper and 2 for Scissors ')
choice = game[int(user)]

print('You chose :')
print(choice)

print('Computer Chose:')
print(computer)

if(computer ==choice):
    print('Its a Draw🐵')
elif(computer == 2 and choice ==0):
    print('You won')
elif(computer == 0 and choice ==2):
    print('You Lostttt')

elif(computer > choice):
    print('You Lose')
elif(computer < choice):
    print('You Win!')

else:
    print('Invalid Input , you lose!')
