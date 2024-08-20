user_word = input("Input any word: ") # asks the user for input
user_word = user_word.upper() # converts input to capital letters

# For Loop for eating the AEIOU
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
    else: # displays the uneaten letters by line
        print(letter)