
"""EX02 - One-Shot Worldle."""

__author__ = "730565191"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
guess: str = input("What is your " + str(len(secret_word)) + "-letter guess? ")

while len(guess) != len(secret_word):
    guess = input("That was not " + str(len(secret_word)) + " letters! Try again: ")

index_check: int = 0
emoji_string: str = ""
character_elsewhere: bool = False
alternate_indices: int = 0

while index_check < len(secret_word):
    if guess[index_check] == secret_word[index_check]:
        emoji_string = emoji_string + GREEN_BOX
    else:
        while character_elsewhere is False and alternate_indices < len(secret_word):
            if secret_word[alternate_indices] == guess[index_check]:
                character_elsewhere = True
            alternate_indices = alternate_indices + 1
        if character_elsewhere is True:
            emoji_string = emoji_string + YELLOW_BOX
        else:
            emoji_string = emoji_string + WHITE_BOX
        character_elsewhere = False
        alternate_indices = 0
    index_check = index_check + 1 
print(emoji_string)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")