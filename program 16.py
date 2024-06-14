str1 = input("Enter any string : \n")
count = 0
freq_dict = {}
for character in str1:
    if character in freq_dict:
        freq_dict[character] += 1
    else:
        freq_dict[character] = 1
print(freq_dict)