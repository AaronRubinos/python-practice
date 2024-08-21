my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

res = []
[res.append(x) for x in my_list if x not in res]

print("The list with unique elements only:")
print(res)

