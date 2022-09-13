"""EX03 - A Completed Wordle Program"""

__author__ = "730565191"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn_counter: int = 1
    while turn_counter < 6:
        print(f"=== Turn {turn_counter}/6 ===")
        stored_guess: str = input_guess(len(secret_word))
        print(emojified(stored_guess, secret_word))
        if stored_guess == secret_word:
            print(f"You won in {turn_counter}/6 turns!")
        else:
            turn_counter += 1
    if turn_counter == 6 and stored_guess != secret_word:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char (input_guess, char) -> bool: 
    """Given a word and character, this definition and nested while loop determines if said character exists in said word."""
    assert len(char) == 1
    idx_counter: int = 0
    contains_char = False
    while idx_counter < len(input_guess):
        if char == input_guess[idx_counter]:
            return True
            idx_counter += 1
        else:
            idx_counter += 1
        if idx_counter == len(input_guess):
            return False
    return contains_char
    
def emojified (input_guess, secret_word) -> str: 
    """Given a secret word and a guessed word of the same length, the definied string 'emojified' will print out the correct corresponding colored emoji boxes as it would appear in a wordle game."""
    idx_counter = 0
    assert len(input_guess) == len(secret_word)
    emojified = "" 
    while idx_counter < len(secret_word):
        if input_guess[idx_counter] == secret_word[idx_counter]:
            emojified += GREEN_BOX 
            idx_counter += 1
        elif contains_char(secret_word, input_guess[idx_counter]) == True:
            emojified += YELLOW_BOX
            idx_counter += 1
        else:
            emojified += WHITE_BOX
            idx_counter += 1
    return emojified


def input_guess(expected_length) -> str:
    input_guess = input(f"Enter a {expected_length} character word: ")
    while len(input_guess) != expected_length:
        input_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    if len(input_guess) == expected_length:
        return input_guess


if __name__ == "__main__":
    main()