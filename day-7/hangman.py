import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


#1
choosen_word = random.choice(word_list)

#2
guess = input('Enter a letter to check:\n').lower()

#3
for i in range(0, len(choosen_word)):
    if(choosen_word[i] == guess):
        print('Right')
    else:
        print('Wrong')
        

