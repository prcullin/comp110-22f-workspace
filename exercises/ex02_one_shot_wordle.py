"""EX02 - One-Shot Worldle (Loops)!"""

__author__ = "730565191"

secret_word: str = "knoll"

six_letter_guess: str = input("What is your " +str(len(secret_word)) +"-letter guess? ")

while len(six_letter_guess) != len(secret_word):
  six_letter_guess: str = input("That was not " +str(len(secret_word)) +" letters! Try again: ")

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

index_check: int = 0
resulting_emoji: str = ""
character_exists_elsewhere: bool = False
alternate_indices: int = 0

while index_check < len(secret_word):
    if six_letter_guess[index_check] == secret_word[index_check]:
        resulting_emoji = resulting_emoji + GREEN_BOX
    else:
        while character_exists_elsewhere == False and alternate_indices < len(secret_word):
            if secret_word[alternate_indices] == six_letter_guess[index_check]:
                character_exists_elsewhere = True
            alternate_indices = alternate_indices + 1
        if character_exists_elsewhere == True:
            resulting_emoji = resulting_emoji + YELLOW_BOX
        else:
            resulting_emoji = resulting_emoji + WHITE_BOX
        character_exists_elsewhere = False
        alternate_indices = 0
    index_check = index_check + 1
    
print(resulting_emoji)


if six_letter_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Try again soon!")
