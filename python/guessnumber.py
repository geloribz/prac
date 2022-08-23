import random

def guess(x):
    rand_number = random.randint(1,x)
    guess = 0
    while guess != rand_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < rand_number:
            print('Sorry, guess again. Too low.')
        elif guess > rand_number:
            print('Sorry, guess again. Too high.')
    print(f'Congrats! You have guessed the number: {rand_number}')

def com_guess(x):
    lowval = 1
    highval = x
    feedback = ''
    while feedback != 'c':
        if lowval != highval:
            guess = random.randint(lowval,highval)
            feedback = input(f"Is {guess} correct? Too high (H), Too low (L), or Correct (C)?: ").lower()
        else:
            guess = lowval
            feedback = 'c'
        if feedback == 'h':
            highval = guess-1
        elif feedback == 'l':
            lowval = guess+1
    print(f"The computer guessed {guess}! It's correct!")

com_guess(6)
