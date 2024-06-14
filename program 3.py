a = int(input("Enter any number : \n"))
num = a
fact = 1
for i in range(1, num+1):
    fact = fact*i
    i += 1
print("Factorial of", num, "is", fact)