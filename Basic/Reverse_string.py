
'''using loop'''
# time o(n), space O(1)

# def reverse_string(string):
#     str = ''
#     for i in string:
#         str = i+ str
#     return str

# print(reverse_string('hello world'))

''' using recursion'''
# time O(n), spcae O(n)

# def reverse_string(str):
#     return str if len(str) == 0 else reverse_string(str[1:]) + str[0]

# print(reverse_string('Hello world'))
# print(reverse_string('Good morning'))

'''using index sliceing'''
# def reverse_string(str):
#     return str[::-1]


# print(reverse_string('Hello world'))
# print(reverse_string('Good morning'))


# def reverse_string(str):
#     return ''.join(reversed(str))

 
# print(reverse_string('Hello world'))
# print(reverse_string('Good morning'))


'''using list comprehension'''

# def reverse_string(str):
#     return ''.join([str[i] for i in range(len(str)-1, -1, -1)])
 
# print(reverse_string('Hello world'))
# print(reverse_string('Good morning'))


# def reverse_string(str):
#     s = ''
#     for i in str:
#         print(i)
#         s = i+s
#     print(s)

# reverse_string('hello')
 

# def reverse_list(arr):
   
#     # return list(reversed(arr))
#     # return arr[::-1]
#     # return [arr[i] for i in  range(len(arr)-1, -1, -1)]

# print(reverse_list([1, 3, 5, 6, 10]))
# print(reverse_list([0, 10, 30, 50, 70, 90]))


# a = [10, 20, 25, 30, 35]
# b = [40, 45, 60, 75, 90]

# ans = []
# for i in a:
#     if i&1:
#         ans.append(i)

# for j in b:
#     if j&1:
#         ans.append(j)

# print('new list:', ans)


# for i in range(5, 0, -1):
#     print('* ' *i)


