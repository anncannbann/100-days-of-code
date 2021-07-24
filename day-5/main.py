#for loop
'''
fruits= ['apple','orange','banana']
for fruit in fruits:
    print(fruit)
'''
'''
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total =0
no=0

for i in range(0,len(student_heights)):
    total += student_heights[i]
    no +=1
avg = round(total/no)
print(f'Avg height is {avg}')
'''
