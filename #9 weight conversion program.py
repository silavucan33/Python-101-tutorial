# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds (K or L): ")


if unit == "K":
    weight = weight * 2.205
    birim = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {birim}")
elif unit == "L":
    weight = weight / 2.205
    birim = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {birim}")
else:
    print(f"{unit} was not valid")


##"print(f"Your weight is..." "it should not be at the end because the user would get a result even when he enter a wrong unit


