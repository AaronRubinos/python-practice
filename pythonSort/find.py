my_list = [] # empty list
size = int(input("Enter the number of elements in the list: "))

while True:
    found = False
    for i in range(size):
        value = float(input("Enter the values: ")) # Prompts the user to input values for the list
        my_list.append(value) # adds the values in side the list
    
    to_find = float(input("Enter the value that you want to find: ")) # Prompts the user for the value to find
        
    for j in range(len(my_list)):
        found = my_list[j] == to_find
        if found == True:
            break
 
    if found == True:
        print("Element found at index", j)
        break
    else:
        print("absent")
        break
