# my_list = [] # Empty list
# swapped = True # assume true for while loop
# num = int(input("How many elements do you want to sort: ")) # Input how many elements from the user

# for i in range(num): # Numbers of iteration base on the input of the user
#     val = float(input("Enter a list element: ")) # Values that'll be putted in the list
#     my_list.append(val) 

# while swapped: 
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nSorted:")
# print(my_list)

my_list = [] # Empty list
num = int(input("How many elements do you want to sort: ")) # Input how many elements from the user

for i in range(num): # Numbers of iteration base on the input of the user
    val = float(input("Enter a list element: ")) # Values that'll be putted in the list
    my_list.append(val) 
    
my_list.sort()
print(my_list)

my_list.reverse()
print(my_list)


