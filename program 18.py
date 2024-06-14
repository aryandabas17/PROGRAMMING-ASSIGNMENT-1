str1 = input("Enter first string : \n")
str2 = input("Enter second string : \n")
str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()
if sorted(str1) == sorted(str2):
    print("This pair of strings is Anagram.")
else:
    print("This pair of strings is not Anagram.")