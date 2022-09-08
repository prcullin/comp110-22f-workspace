"""EX01 - Chardle - A cute step towards Wordle."""

__author__ = "730565191"

five_character_word: str = input("Enter a 5-Character word: ")
if len(five_character_word) != 5:
    print("Error: Word must contain 5 characters.")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + single_character, "in " + five_character_word)

if single_character == five_character_word[0]:
    print(single_character, "found at index 0")
if single_character == five_character_word[1]:
    print(single_character, "found at index 1")
if single_character == five_character_word[2]:
    print(single_character, "found at index 2")
if single_character == five_character_word[3]:
    print(single_character, "found at index 3")
if single_character == five_character_word[4]:
    print(single_character, "found at index 4")

instances_of_character: int = five_character_word.count(single_character)

if instances_of_character == 1:
    print(instances_of_character, "instance of " + single_character, "found in " + five_character_word)
if instances_of_character > 1:
    print(instances_of_character, "instances of " + single_character, "found in " + five_character_word)
else:
    print("No instances of " + single_character, "found in " + five_character_word)
