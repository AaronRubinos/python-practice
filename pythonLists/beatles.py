beatles = [] #empty list

# step 1
print("Step 1:", beatles)


beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# step 2
print("Step 2:", beatles)

for i in range(2):
    user = input()
    beatles.append(user)
    i += 1
    
# step 3
print("Step 3:", beatles)

for n in range(0, 2):
    del beatles[n - 2]
    n += 1

# step 4
print("Step 4:", beatles)

beatles.insert(0, "Ringo Starr")

# step 5
print("Step 5:", beatles)

# testing list legth
print("The Fab", len(beatles))

