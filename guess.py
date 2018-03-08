# Guess the number game
import random

guessesTaken = 0

print("Hello nerd, What's your name?")
playerName = input()

number = random.randint(1, 20)
print('Well, ' + playerName + " I'm thinking of a number between 1 and 20")

for guessesTaken in range(6):
    print('Give it a shot')
    guess = input()
# We need to convert this string into an integer
    guess = int(guess)

    if guess < number:
        print('Lil low')

    if guess > number:
        print('Lil high')

    if guess == number:
        break
# A break statement tell the execution to jump out of the for block.
if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Well done ' + playerName + ', you guessed my secret number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Better luck next time ' + playerName + ', the number I was thinking of was ' + number + '.')





