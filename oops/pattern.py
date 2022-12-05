
 
# *
# * *
# * * *
# * * * *
# * * * * *


# n = int(input('>>>'))
# for i in range(1, n+1):
#     print('* '* i) 


# n = int(input('>>>'))

# for i in range(n, 0, -1):
#     print('* '*i)


# n = int(input(">>> "))
# for i in range(1, n+1):
#     if(i&1): print('* ' * i)
 

# n = int(input('>>> ')) 
# s = '*'

# for i in range(n):
#     print(s*i).rjsut(n-1) + s+ (s*i).ljust(n-1)

# side=int(input())
# c='*'
# for i in range(side):
#     print((c*i).rjust(side-1)+c+(c*i).ljust(side-1))


# n = int(input('>>> '))
# s = '*'

# for i in range(n):
#     print(end=' ')
#     print((s*i).rjust(n-1) + s + (s*i).ljust(n-1))


# n = int(input('>>> '))
# x = ['x'*i + '* ' *(n-i) for i in range(n)]
# for i in x: print(i)


# n=int(input())
# x=[" "*i+"* "*(n-i) for i in range(n)]
# for i in x: print(i)

# n = int(input('>>> '))

# res = [' '*i + '* '*(n) for i in range(n)]
# for x in res: print(x)



# ======================================================

# #Question: 1
# def calculate_pow(base, pow):
#     return base ** pow

 
# a , b = map(int, input('Enter the numbers:').split())
# print(calculate_pow(a, b))

# #another way..
# import math
# def find_pow(base, power):
#     return math.pow(base, power)
 
# a , b = map(int, input('Enter the numbers:').split())
# print(find_pow(a, b))


# # Question:2
# def find_sum(a, b, c):
#     return a + b + c

# a, b, c = map(float, input('Enter 4 numbers:').split('-'))
# print(find_sum(a, b, c))


# Questin:3

# def reverse_string(str):
#     return ' '.join(word[::-1] for word in str.split(' '))


# str = input('>>> ')
# print(reverse_string(str))
 


# Question: 6
# def func(arg1, arg2, arg3=4, arg4=5):
#     print(arg1, arg2, arg3, arg4)
  

# func(6, 7)
# func(4, 5, arg3=6)
# func()
# func(3, 4, arg2=1)



# 1. 6 7 4 5
# 2. 4 5 6 5
# 3. missing argument (arg1, agr2)
# 4. arg2 given multiple values(argument) 
 

# Question:7

# class Subset:
#     def sort_list(self,List):
#         return self.find_subset([], sorted(List))
    

#     def find_subset(self, curr, List):
#         if List:
#             return self.find_subset(curr, List[1:]) + self. find_subset(curr + [List[0]], List[1:])
#         return [curr]
    
# List = list(map(int, input().split()))
# print(Subset().sort_list(List))

# Question:8

# def findPair(arr, target) :
#     arr.sort()
#     (low, high) = (0, len(arr)-1)
#     while low < high:
#         if(arr[low] + arr[high] == target):
#             print('pair found:', (arr[low], arr[high]))
#             return
        
#         if arr[low] + arr[high] < target:
#             low = low +1
#         else:
#             high = high +1
    
#     print("No pair found")


# if __name__ == '__main__':
#     arr =  [10,20,10,40,50,60,70]

#     target = 50

#     print(findPair(arr, target))


# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     num_lst = list(range(len(nums)))

#     for indx, num in enumerate(num_lst):
#         for num_other in num_lst[indx+1:]:
#             if nums[num] + nums[num_other] == target:
#                 return [num, num_other]
#             else: 
#                 continue
#     return None


# numbers= [10,20,10,40,50,60,70]
# target=50 

# print(twoSum(numbers, target))


# def findPair(arr, target) :
#     arr.sort()
#     (low, high) = (0, len(arr)-1)
#     while low < high:
#         if(arr[low] + arr[high] == target):
#             print('pair found:', (arr[low], arr[high]))
#             return
        
#         if arr[low] + arr[high] < target:
#             low = low +1
#         else:
#             high = high +1
    
#     print("No pair found")

# numbers= [10,20,10,40,50,60,70]
# target=50 
# print(findPair(numbers, target))

 


# def two_sum(A, S):
# 	pairs = []
# 	for i in range(len(A)):
# 		for j in range(i+1, len(A)):
# 			if A[i] + A[j] == S:
# 				pairs.append([i+1, j+1])

# 	return pairs

# numbers= [10,20,10,40,50,60,70]
# target=50 

# print(two_sum(numbers, target))


# class Solution():
#     def twoSum(self,nums, target):
#         ans = {}
#         for i, num in enumerate(nums):
#             if target - num in ans:
#                 return [ans[target - num], i+1]
#             ans[num] = i+1
#         return
 

# numbers= [10,20,10,40,50,60,70]
# target=50 
# print(Solution().twoSum(numbers, target))


# # Quetion: 10
# import math
# class Distance():
#     def __init__(self, x1:int = 0, y1:int = 0, x2:int = 0, y2:int = 0):
#         self.x1 = x1
#         self.y1 = y1 
#         self.x2 = x2 
#         self.y2 = y2 
    
#     def get_distance(self):
#          return math.sqrt((math.pow((self.x2 - self.x1), 2)) + (math.pow((self.y2 - self.y1), 2)))

# # x1, y1, x2, y2 = map(int, input().split()) 
# # d = Distance(x1, y1, x2, y2)
# # print(round(d.get_distance(), 2)) 


# x1, y1, x2, y2 = map(int, input().split()) 
# print('Distance:', Distance(x1, y1, x2, y2).get_distance())



# #Question: 9
# class Solution:
#     def __init__(self, x:int, n:int):
#         self.x = x 
#         self.n = n 

#     # find sum... 
#     def sum(self):
#         return self.x + self.n 
    
#     def pow(self):
#         res = 0
#         if self.n == 0:
#             return 1 
#         else:
#             for i in range(1, self.n+1):
#                 res = self.x ** i 
#             return res 
            

# x , n = map(int, input().split())
# s = Solution(x, n)
# print(s.sum())
# print(s.pow()) 


# class Solution:
#     def all_subsets(self,b):
#         b = b[::-1]
#         if len(b)==1: return [[], b] 
#         else:
#             s = self.all_subsets(b[1:])  
#             return sorted(s + [e + [b[0]] for e in s], key=len) 
        

# List = list(map(int, input().split()))
# print(Solution().all_subsets(List))




# class Subset:
#     def sort_list(self,List):
#         return self.find_subset([], sorted(List))
    

#     def find_subset(self, curr, List):
#         if List:
#             return self.find_subset(curr, List[1:]) + self. find_subset(curr + [List[0]], List[1:])
#         return [curr]
    
# List = list(map(int, input().split()))
# print(Subset().sort_list(List))


# #find Circomference of circle
# import math
# r = int(input('>>> '))
# ans = math.pi * 2 * r 
# print(round(ans), 2)

# s = "x3b4U5i2"
# s = [i for i in s]
# s = [s[i]*int(s[i+1]) for i in range(0, len(s), 2)]
# s = sorted(s, key=lambda x: (x.lower(), x.isupper()))
# print("".join(s))


# # Question: 4:
# def solve(str):
#     str = [str[i] *int (str[i+1]) for i in range(0, len(str), 2)]
#     str = sorted(str, key=lambda x: (x.lower(), x.isupper()))
#     return ''.join(x for x in str)
 

# str = input('>>> ')
# print(solve(str)) 
# print(solve("x3b4U5i2"))

# def solve(str):
#     str = str.split()
#     print(*str[::-1])

# for _ in range(int(input())):
#     str = input() 
#     solve(str) 

# n = int(input()) 
# for i in range(0, n):
#     x = input()
#     p= x.split()[::-1]
#     print(' '.join(p))


# class Dog:
#     def walk(self):
#         return "*walking*"
#     def speak(self):
#         return "Woof!"
# class JackRussellTerrier(Dog):
#      def speak(self):
#          return "Arff!"
# bobo = JackRussellTerrier()
# print(bobo.speak())


