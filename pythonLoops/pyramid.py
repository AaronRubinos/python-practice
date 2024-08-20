# blocks = int(input("Enter number of blocks: "))

# for i in range(blocks + 1):
#     for j in range(blocks + 1):
#         height = j / 2
# if height % 2 == 0:
#     height = height / 2

# print("The height of the pyramid:", int(height))

blocks = int(input("Enter number of blocks: "))

height = 0
layer = 1

while blocks >= layer:
    blocks -= layer
    height += 1
    layer += 1

print("The height of the pyramid:", height)
