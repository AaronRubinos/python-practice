def strange_function(n): # function name with it's parameter variable
    if(n % 2 == 0): # the n here is a varialbe that could only be used inside the function
        return True # the return in the function is paired with it's expression if it should return a specific result

x = strange_function(4) # This is an invocation of the function with it's parameter and as well as the storing of it's return value

print(x) # Prints True

# You could directly print the invoked function 
print(strange_function(2)) 
print(strange_function(1))
