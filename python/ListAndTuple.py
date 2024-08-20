
#+ INDEX -  0       1       2       3          4
#- INDEX -  -5      -4      -3      -2         -1
courses = ["BSIT", "BSCS", "BLIS"]

#print(courses[1:4]) 

#Assigning List Items
#courses[0] = "Hatdog"
#courses[2] = "Cheesedog"

#print(courses)

#print the LENGTH
#print(len(courses))

#COUNT prints how many occurences of one value inside a list
#print(courses.count("BSCS"))

#append()
#courses.append("Hatdog")
#courses.append("Cheesedog")
#print(courses)

#insert()
#courses.insert(1, "Hatdog")
#print(courses)

#remove()
#courses.remove("BSIT")
#print(courses)

#pop()
#courses.pop()
#courses.pop(1)
#print(courses)

#del
#del courses[0]
#del courses
#print(courses)

#clear()
#courses.clear()
#print(courses)

#copy()
#courses.pop()
#copy = courses.copy()
#print(copy)

#Combining list by ADDING
#food = ["Hatdog", "Cheesedog"]
#coursesFood = courses + food
#print(coursesFood)

#Combining list by EXTEJD
#food = ["Hatdog", "Cheesedog"]
#courses.extend(food)
#print(courses)

#Combining list by append()
#food = ["Hatdog", "Cheesedog"]
#courses.append(food)
#print(courses)

#REVERSE LIST items
#courses.reverse()
#print(courses)

#SORT List items. ascending order is the default sort order
#alphabet = ["5", "1", "6", "2"]
#alphabet.sort()
#print(alphabet)

#NESTED Lists
        #       0       1       2                        3
#courses = ["BSIT", "BSCS", "BLIS", [["SHAMPOO", "ALCOHOL"], "CHEESEDOG"]]
        #                                       3, 0            3, 1
#print(courses[3][1])

#TUPLES the same as LISTS
#SYNTAX: identifier = (value1,value2,valu3)
#Limitations:
#can be READ
#can be COMBINED
#can be DELETED COMPLETELY
#can't be ASSIGNED
#can't be DELETED ONE BY ONE
#courses1 = ("BSIT", "BSCS", "BLIS")
#courses1[0] = "Hatdog"
#print(courses1[0])

#CASTING tuples and lists
#Convert List to Tuple
    #tuple(list)
#Convert Tuple to List
    #list(tuple)
#courses1 = ["BSIT", "BSCS", "BLIS"]
#courses1 = tuple(courses1)
#print(courses1)