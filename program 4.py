import time

name = input("Enter your name : \n")
timestamp = int(time.strftime("%H"))
if 00 <= timestamp < 12:
    print("Good morning", name)
elif 12 <= timestamp < 15:
    print("Good afternoon", name)
elif 15 <= timestamp < 20:
    print("Good evening", name)
else:
    print("Good night", name)