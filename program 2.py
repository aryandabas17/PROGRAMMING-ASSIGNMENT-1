try:
    a = int(input("Enter any number : \n"))
    if a % 2 == 0:
        print("The given number is even.")
    elif a % 2 != 0:
        print("The given number is odd.")
    else:
        print("Invalid input.")
except ValueError:
    print("Invalid input.")