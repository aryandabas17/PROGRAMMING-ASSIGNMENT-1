import string
str1 = input("Enter any string :\n")
cleaned_string = ""
for char in str1:
    if char not in string.punctuation:
        cleaned_string += char
print(cleaned_string)