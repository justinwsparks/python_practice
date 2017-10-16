# program to play a number guessing game

import random
print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1, 20)
print('Well.' + name + ' I am thinking of a number between 1 and 20.')
print('Can you guess what it is?')

# ask the player to guess 6 times.

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # this condition is the correct guess!

if guess == secretNumber:
    print('Holy crap! You little cheater! Tell the truth ' + name + ' ... How did you know?')
else:
          print('Nope. the number I was thinking of was ' + str(secretNumber))