try:
    list1 = []
    while True:
        choice = input("Enter 'yes' to give inputs to the list or 'quit' to quit :\n")
        if choice.upper() == "YES":
            try:
                n = int(input("Enter number of numbers you want into the list :\n"))
                for i in range(1, n+1):
                    num = int(input(f"Enter number {i} :\n"))
                    list1.append(num)
                sum1 = 0
                for num in list1:
                    sum1 += num
                print("Sum of all the elements provided is :", sum1)
                print("==== CODE EXECUTION SUCCESSFUL ====")
                break
            except ValueError:
                print("Invalid Input !!")
        elif choice.upper() == "QUIT":
            print("Exited the code !!")
        else:
            print("Invalid choice !!")
except MemoryError:
    print("Memory assignment unsuccessful !!")