lines = []
print("Enter line or just press enter to finish : \n")
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
print("\nYou entered : ")
for line in lines:
    print(line)