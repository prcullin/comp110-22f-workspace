"""A introductory program serving as an 'Eightball' game."""

from random import randint

question: str = input("What is your yes/no question? ")
response: int = randint(0,2)

if response == 0:
    print("Yes, definitely.")
else:
    if response == 1:
        print("Ask again later.")
    else:
        print("My sources say no.")