num = int(input("Enter any number : \n"))
a = num
sum_of_digits = 0
while a > 0:
    digit = a % 10
    sum_of_digits += digit
    a = a // 10
print("Sum of digits of", num, "=", sum_of_digits)