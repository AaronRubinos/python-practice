kilometers = float(input("Enter Kilometers: "))
miles = float(input("Enter Miles: "))

miles_to_kilometers = miles * 1.609344
kilometers_to_miles = kilometers * 0.62137

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
