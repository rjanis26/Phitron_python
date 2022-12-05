
# str = 'Bangladesh'
# length = 0
# for i in str:
#     print(i, end=' ')
#     length +=1

# print()
# print('Length of string: ', length)
 
# print(str)
 

# str = 'my name is anisul islam &&$@@'
# # print(str.capitalize())
# # print(str.title())
# # print(str.upper())
# # print(str.lower())
# print(str.casefold())


#user input in python

# num = int(input("Enter the name: "))
# print(num+3)
# str = input("Enter your name: ")
# print(str)


 


# fruits = ['Apple', 'Mango', 'Rabbit']
# print(fruits)

# for i in fruits:
#     print(i)

# print('fist:', fruits[-1])
# print('second:',fruits[2])


# print(num)

# sum = 0
# for i in num:
#     sum += i

# print('Sum of list:', sum)


''' Reverese the digit'''

# n = 345910
# print('Given number:', n)

# while n:
#     digit = n%10
#     n//= 10

#     print(digit,end='')

'''multiplication table'''
  
# for i in range(1, 11):
#     for j in range(1,11):
#         print(i*j, end=' ')
#     print()
 

# def find_sum(n):
#     total = 0
#     for i in n:
#         total += i
#     return total
#     # return sum(n)

# print('new sum:',find_sum([1,2, 3, 4, 5]))

  
# def find_multi(nums):
#     total = 1
#     for num in nums:
#         total *= num
#     return total

# print('multiplications:', find_multi([8, 2, 3, -1, 7]))


# def reverse_string(str):
#     s = ''
#     for string in str:
#         s = string + s
#     return s

# print(reverse_string('hello'))
 
# def reverse_string(str):
#     revString = ''
#     n = len(str)-1
#     while n:
#         revString += str[n]
#         n -= 1
#     return revString

# print(reverse_string('hello wrold'))
 

# n = 13489
# print('Given number:', n)
# str_x = str(n)
# print(str_x[::-1])



# str = input('Enter the strig:')
# if str[:len(str)] == str[::-1]:
#     print('Yes\n')
# else:
#     print('No\n')
  

# def is_palindrome(n):
#     return True if str(n) == str(n)[::-1] else False
#     # return True if str[:len(str)] == str[::-1] else False

# print(is_palindrome('hello'))
# print(is_palindrome('wow'))
# print(is_palindrome(121))
# print(is_palindrome(5252))



# print('Table of 1-10\t')
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i, 'X', j, '=', i*j)
#     print('\n')



# for i in range (1,11) :
#     number = 0
#     for j in range(1,11) :
#         number += i
#         print(number, end=' ')
#     print("\t\t")


# [print(' '.join([str(i*j) for i in range(1,11)])) for j in range(1,11) ]  #exercise 13 


# def reverse_n(n):
#     return int(str(n)[::-1])

# print(reverse_n(13429))

 
# def merge_two_lsit(arr, brr):
#     ans = []
#     for i, j in zip(arr, brr):
#         if i&1:
#             ans.append(i)
#         if j&1:
#             ans.append(j)
#     return ans


# print(merge_two_lsit([1, 4, 5, 3], [11, 2, 4, 13]))
