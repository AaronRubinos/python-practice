#Original contents
numbers = [111, 7, 2, 1]
print(len(numbers))
print("Original contents:", numbers)

###

numbers.append(4)

print(len(numbers))
print("Appended value added:", numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print("Inserted value added:", numbers)

###

numbers.insert(1, 333)
print(len(numbers))
print("Inserted value added:", numbers)
