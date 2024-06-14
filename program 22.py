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
                print("Maximum value in this list is :", max(list1))
                print("Minimum value in this list is :", min(list1))
                break
            except ValueError:
                print("Invalid input !!")
except MemoryError:
    print("Memory assignment unsuccessful !!")