list1 = []

while True:
    choice = input("Enter 'yes' to give inputs to the list or 'quit' to quit :\n")
    if choice.lower() == 'yes':
        try:
            n = int(input("Enter number of elements you want in the list :\n"))
            for i in range(1, n + 1):
                num = input(f"Enter element {i} :\n")
                list1.append(num)

            while True:
                choice1 = input(
                    "Enter 'f' to find the number of occurrences of a particular element in this list or 'quit' to quit :\n")
                if choice1.lower() == 'f':
                    character = input("Enter the character whose number of occurrences you wish to find :\n")
                    count = 0
                    for char in list1:
                        if character == char:
                            count += 1
                    print(f"Frequency of {character} is : {count}")
                elif choice1.lower() == 'quit':
                    break
                else:
                    print("Invalid choice !!")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    elif choice.lower() == 'quit':
        break
    else:
        print("Invalid choice! Please enter 'yes' or 'quit'.")