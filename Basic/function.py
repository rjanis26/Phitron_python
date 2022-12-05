
# def helper(x, y):
#     return x if x > y else y

# def max_of_three(x, y, z):
#     return helper(x, helper(y,z))

# a, b, c = map(int, input().split())
# print(max_of_three(a, b, c))

# def max_of_three(a, b, c):
#     return max(a, b, c)


# a, b, c = map(int, input('Enter three num:').split())
# print(max_of_three(a, b, c))
# # print(max_of_three(10, 20, 50))


# def max_of_three(a, b, c):
#     largest = a
#     if b > largest:
#         largest = b
#     if  c > largest:
#         largest = c
    
#     return largest


# a, b, c = map(int, input('Enter three num:').split())
# print(max_of_three(a, b, c))


# def find_sum(List):
#     return sum([x for x in List if not x&1])

# List = list(map(int, input('Enter the list:').split()))
# print(find_sum(List))
# print(find_sum([1, 2, 3, 4, 5, 6]))


# def cumulative_product(List):
#     val = 0
    # return [(val:= val+x) for x in List]
    
    # prod = 1
    # return [(prod:= prod*x) for x in List]

# print(cumulative_product([1, 2, 3, 4, 5]))


# import math
# def solve(List):
#     return ([math.prod(List[:x]) for x in range(1, len(List)+1)])

# print(solve([1, 2, 3, 4, 5]))
# print(solve([1, 3, 2, 3]))


# def textReplace():  
#   text = '000 this is 001 some 002 text 003 '
#   word = ['foo', 'bar', 'that', 'these']
#   for a in word:    
#     for y, w in enumerate(text):      
#       x = "00"+str(y)
#       text = text.replace(x, a)
#   print(text)

# textReplace()

# def clean_string(text):
#     str = ""
#     for s in text:
#         if s.isalpha():
#             str += s
#     return str
    
# s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"
# output = clean_string(s)
# print(output)

