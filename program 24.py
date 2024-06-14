choice = input("Enter 'c' to access Calculator or 'q' to Quit :\n")
if choice.upper() == "C":
    num1 = int(input("Enter number 1 :\n"))
    choice1 = input("Enter '+' to add, '-' to subtract, '*', to multiply, '/' to divide :\n")
    num2 = int(input("Enter number 2 :\n"))
    try:
        match choice1:
            case "+":
                print(f"Sum of {num1} and {num2} is : {num1 + num2}")
            case "-":
                print(f"Difference of {num1} and {num2} is : {num1 - num2}")
            case "*":
                print(f"Product of {num1} and {num2} is : {num1 * num2}")
            case "/":
                print(f"Quotient of {num1} and {num2} is : {round(num1 / num2, 4)}")
        print("==== Code execution successful ====")
    except ValueError:
        print("Invalid input !!")
elif choice.upper() == "Q":
    print("Exited the code !!")