import random
from words import words #import the list
from lives_vis import lives_vis #imports the dictionary
import string #importing string library function

def get_val_word(words):
    word = random.choice(words) #return random element in the list of 'words'
    while '-' in word or ' ' in word: #will pick again if the word has these characters
        word = random.choice(words) 
    return word.upper()

def hangman():
    word = get_val_word(words) #return a word from 'words' list as a string and it is all in uppercase
    word_letters = set(word) # letters in the string variable word as elements in a list, all in uppercase
    alphabet = set(string.ascii_uppercase) # letters in the alphabet as elements in a list, all in uppercase. Built-in method that can be used on strings
    used_letters = set() # what user has guessed, starts out empty at first

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) ---> 'a b cd'
        print('You have used these letters: ', ' '.join(sorted(used_letters)))

        # what current word is (ie W _ R D)
        word_list = [aer if aer in used_letters else '-' for aer in word] #aer here is just the name for the placeholder
        print(lives_vis[lives]) #finds the value counterpart of the key that has the same value as the lives variable
        print('Current word ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter) #going to length of zero breaks while loop
                print('')
            else:
                lives = lives - 1 # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')
        elif user_letter in used_letters:
            print('\nYou have already used that.')
        else:
            print('\nInvalid character.')

    # gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print(lives_vis[lives])
        print('You died, sorry. The word was', word)
    else:
        print('You got the word:', word, '!!')

hangman()
