number = 7
user_input = input("Enter 'y' if you want to play the game: ")

if user_input == "y":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    else:
        print("Sorry. You are wrong.")
