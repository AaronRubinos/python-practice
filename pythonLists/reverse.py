
# Reversing the values of the variables
# variable_1 = 1
# variable_2 = 2

# auxiliary = variable_1
# variable_1 = variable_2
# variable_2 = auxiliary

# Much effective and efficient way. In this way you'll remove the use of another temp variable or the aux variable
# variable_1 = 1
# variable_2 = 2

# variable_1, variable_2 = variable_2, variable_1


# You could also use in list
# my_list = [10, 1, 8, 3, 5]

# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]

# print(my_list)

# You could also use this in the for loop, this is effective for lists that has a big value
my_list = [10, 1, 8, 3, 5]

for i in range(len(my_list) // 2):
    my_list[i], my_list[len(my_list) - i - 1] = my_list[len(my_list) - i - 1], my_list[i]

print(my_list)



