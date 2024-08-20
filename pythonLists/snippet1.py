numbers = [6, 20 , 2, 7, 27, 3]
print("Original contents: ", numbers)

numbers[5] = 21 #Declaring a new value in an element
print("Previous contents: ", numbers)

numbers[2] = numbers[1] #Copies the value of another element to another
print("New contents: ", numbers)

print("List length: ", len(numbers)) #Prints the length of the list

del numbers[2] #Deletes the third element in the list

print("New list length: ", len(numbers))
print("New list contents: ", numbers)

#You can use negative indices
print(numbers[-1]) #This will print the last element in the list
print(numbers[-2]) #This will print the one before last in the list





