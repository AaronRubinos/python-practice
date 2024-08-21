# def is_prime(n):
#     for i in range(2, int(1 + n ** 0.5)):
#         if n % i == 0:
#             return False
#     return True

# num = int(input("Enter value: "))
# x = is_prime(num)

# if x == True:
#     print("The number", num, "is a prime number")
# else:
#     print("The number", num, "is not a prime number")
    
def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

