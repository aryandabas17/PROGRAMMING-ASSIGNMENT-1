try:
    newfile = open("input.txt", "w")
    data = input("Enter the data you wish to write into the file : \n")
    newfile.write(data)
except FileExistsError:
    print("File already exists.")