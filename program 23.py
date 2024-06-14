import math
choice = input("Enter 'f' to convert temperature from Celsius to Fahrenheit or 'c' to covert temperature from Fahrenheit to Celsius :\n")
if choice.upper() == "F":
    temperature = int(input("Enter the temperature in Celsius :\n"))
    Fahrenheit = (temperature * 1.8) + 32
    print(f"{temperature} in Celsius is {round(Fahrenheit, 4)} in Fahrenheit")
elif choice.upper() == "C":
    temperature = int(input("Enter the temperature in Fahrenheit :\n"))
    Celsius = (temperature - 32) * 0.5555555556
    print(f"{temperature} in Celsius is {round(Celsius, 4)} in Fahrenheit")
else:
    print("Invalid Input !!")