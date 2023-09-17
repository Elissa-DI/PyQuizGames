import random

number = input('Enter a number: ')
if number.isdigit():
    number = int(number)

    if number <= 0:
        print('Enter a positive number next time😒')
        quit()
else:
    print('Enter a number next time😒')
    quit()

random_number = random.randint(0,number)
guesses = 0

while True:
    guesses += 1
    guessed = input('Guess a number: ')
    if guessed.isdigit():
        guessed = int(guessed)
    else:
        print('Enter a number next time😒')
        continue

    if guessed == random_number:
        print('You got it💪')
        break
    elif guessed > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

if guesses == 1:
    print("You got it with", guesses, "guess")
else:
    print("You got it with", guesses, "guesses")

