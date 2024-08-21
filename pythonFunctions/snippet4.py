def strange_list_fun(n):
    strange_list = []
    
    for i in range(0, n):
        strange_list.insert(0, i)
    
    return strange_list # returns the list 

print(strange_list_fun(5)) # Prints the list [4, 3, 2, 1, 0]

