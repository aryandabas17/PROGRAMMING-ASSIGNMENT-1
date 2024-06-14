from datetime import datetime
current = datetime.now().year
birth_year = int(input("Enter your birth year : \n"))
age = current - birth_year
print("Your age is :", age)