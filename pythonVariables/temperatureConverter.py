print("Fahrenheit to Celsius Converter")

f = float(input("Enter degrees in Fahrenheit: "))
c = float(input("Enter degrees in Celsius: "))

c_to_f = (c * 9/5) + 32
f_to_c = (f - 32) * 5/9

print(f, "Fahrenheit is", round(f_to_c, 2), "Celsius")
print(c, "Celsius is", round(c_to_f, 2), "Fahrenheit")