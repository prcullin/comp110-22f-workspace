"""An example of conditional (if-else) statements."""

SECRET: int = 3

print("Im thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess?"))

if guess == SECRET:
    print("You guessed correctly!!!")
else: 
    print("Sorry, you guessed incorrectly ß:(")

print("Game over")


