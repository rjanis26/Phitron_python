

''' count the nubmer of vowels'''

# str = input("Enter the string:")
# count = 0

# vowels = set("aeiou")

# for element in str:
#     if element in vowels:
#         count += 1
    
# print('Number of vowels:', count)

'''find common letters between two string'''
 

# str1 = input('Enter the first string:')
# str2 = input('Enter the second string:')

# newString = list(set(str1) & set(str2))
# print('Common letters:')
# for i in newString:
#     print(i, end=' ')

 
a = input("Enter the string:")
b = input('Enter the strign:')

newString = list(set(a)^set(b))
for i in newString:
    print(i, end=' ')