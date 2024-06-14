str1 = input("Enter any string : \n")
str2 = input("Enter the substring you wish to check in the string : \n")
if str2 in str1:
    print("Yes", str2, "is present in the string.")
else:
    print("No", str2, "is not present in the string.")