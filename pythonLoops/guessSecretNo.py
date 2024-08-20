# #Read the guessed number
# user = int(input("Guess the secret number: "))

# # 27 terminates 
# while user != 27 :
#     print("Ha ha! You're stuck in my loop!")
        
#     # Reads the next number    
#     user = int(input("Guess again: "))
    
# print("Well done, muggle! You are free now.")

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

#Read the guessed number
user = int(input("Guess the secret number: "))

# terminates when secret_number is inputted 
while user != secret_number :
    print("Ha ha! You're stuck in my loop!")
        
    # Reads the next number    
    user = int(input("Guess again: "))

# Prints when the program is completed    
print("Well done, muggle! You are free now.")
