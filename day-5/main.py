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

#max value without max()
'''
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

maximum = 0
for scores in student_scores:
  if(scores > maximum):
    maximum = scores

print(maximum)
'''
'''
#Gauss
x =0
for i in range(1,101):
  x+=i
print(x)
'''


#sum of even numbers
'''
sum1 = 0
for i in range(1,101):
  if(i%2==0):
    sum1+=i
print(f'Sum is {sum1}')
'''
