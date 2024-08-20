print("Dollar to Euro Currency Exchange")

dollar = float(input("Enter Dollar: "))
euro = float(input("Enter Euro: "))

dollar_to_euro = dollar * 0.92
euro_to_dollar = euro * 1.08

print(dollar, "dollars is", round(dollar_to_euro, 2), "euro/s")
print(euro, "euros is", round(euro_to_dollar, 2), "dollar/s")