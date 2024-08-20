print("Php to Dollar Currency Exchange")

peso = float(input("Enter Peso/s: "))
dollar = float(input("Enter Dollar/s: "))

peso_to_dollar = peso * 0.017
dollar_to_peso = dollar * 58.62

print(peso, "Php is", round(peso_to_dollar, 3), "peso/s")
print(dollar, "USD is", round(dollar_to_peso, 3), "dollar/s")