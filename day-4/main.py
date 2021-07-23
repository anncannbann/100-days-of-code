import random
import my_module as p

'''
#randomisation
x = random.randint(1,10)
print(x)

print(p.pi)


xy = random.random()*5

print(xy)

'''

#heads or tails

'''
toss = random.randint(0,1)

if(toss ==1):
    print('Heads')
else:
    print('Tails')
'''

#lists
'''
lst1 = ['a','b','c']

lst2 =['d','e']

#lst1.extend(lst2)
lst1.extend(['c','d'])
print(lst1)

'''

#Banker ROulette
'''
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# print(names)

#x = names[random.randint(0,len(names)-1)]

x = random.choice(names)
print(f'{x} will be paying the bill today!')

'''

#Treasure Map
'''
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

#print(type(position))
row = int(position[1])-1
column = int(position[0])-1

print(row,column)

map[row][column] ="🟥"

print(f"{row1}\n{row2}\n{row3}")

'''


