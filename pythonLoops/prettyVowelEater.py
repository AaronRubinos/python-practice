word_without_vowels = ""

user_word = input("Input any word: ") # Asks the user for input
user_word = user_word.upper() # Converts the user_word to all CAPS

# For loop for eating the AEIOU
for letter in user_word:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else: # concatenates the uneaten letters in the word_without_vowels variable
        word_without_vowels += letter
        
# Outputs the concatenated uneaten letters
print(word_without_vowels)  