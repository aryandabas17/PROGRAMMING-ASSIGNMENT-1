def read_file():
    filename = input("Enter the filename: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print(f"The file {filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
read_file()
