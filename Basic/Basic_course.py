
# has_pc = True
# has_resource = True

# if has_pc and has_resource:
#     print('You can learn python.')
# else:
#     print("You don't")


# name = input('Enter your name:')

# if len(name) > 11:
#     print('This is too long!')
# elif len(name) < 11:
#     print('This is too short!')
# elif len(name) == 11:
#     print('Thank you '+ str(name))


# fizzbuzz problem....
# def fizzBuzz(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('fizzbuzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print(i)


# n = int(input('Enter your n:'))

# fizzBuzz(n)
# print('****************')
# fizzBuzz(n)
# print('****************')
# fizzBuzz(n)

'''Lambda function'''

# res = (lambda a: a+15)
# print(res(10))


# res = lambda x,y : x*y
# print(res(10, 5))


# def even(arr):
#     return list(filter(lambda x: not x&1, arr))
 
# print(even([i for i in range(1,11)]))


# def oddList(arr):
#     return list(filter(lambda x: x&1, arr))

# print(oddList([i for i in range(1, 11)]))



# def square(arr):
#     return list(map(lambda x: x**2, arr))

# print(square([i for i in range(1,11) if not i&1]))

# def odd_square(arr):
#     return list(map(lambda x: x**2, arr))

# print(odd_square([i for i in range(1,11) if i&1]))

# def find_cube(arr):
#     return list(map(lambda x: x**3, arr))

# print(find_cube([i for i in range(1,11) if not i&1]))
  
# def intersection(arr, brr):
#     return list(filter(lambda x: x in brr, arr))

# print(intersection([i for i in range(1,11)], [1, 2, 4, 8, 9]))


# def rearrange_posNeg(arr):
#     return [x for x in arr if x <0] + [x for x in arr if x >= 0]

# print(rearrange_posNeg([-1, 2, -3, 5, 7, 8, 9, -10]))


# def solve(arr):
#     return [x for x in arr if x >= 0] + [x for x in arr if x<0]

# print(solve([1, 3, -2, 4, -1, -10, 5, 4, 2, 10]))

''' Light On_off project...'''

# check = ''
# light_on = False

# while check != 'sleep':
#     check = input('>').lower()

#     if check =='on':
#         if light_on:
#             print('Light is alreay in on mode.')
#         else :
#             light_on = True
#             print('Light turned on!')

#     elif check == 'off':
#         if not light_on:
#             print('Light is already in off Mode.')
#         else:
#             light_on = False
#             print('Light turn off mode!')
#     elif check == 'sleep':
#         break
 
#     elif check =='help':
#         menu = ['1. On - Light on.', '2. of - Light off.', '3. Sleep - exit program!']
#         for item in menu:
#             print(item.title())
#     else:
#         print("I don't understand your comand!")


# def even_odd(n):
#     return 'odd' if n&1 else 'even'


# n = int(input('Enter the n:'))
# print(even_odd(n))
# print(even_odd(n))

# n = int(input('Enter the n:'))

# if n%2 == 0:
#     print(n, ' is even')
# else :
#     print(n, ' is an odd')


# for i in range(1, 11, 2): print(i, end=' ')
 
# count = 0
# for i in range(1, 11, 2):
#     print(i, end=' ')
#     count +=1
# print('Total:' + str(count))


# for i in range(1, 6):
#     print('* ' * i)
 
# for i in range(5, 0, -1):
#     print('* ' * i)


# for i in range(1, 6):
#     for j in range(1, 6):
#         print(f'[{i}, {j}]')


# for i in [5, 1, 3, 1, 5]:
#     print('# '*i)

 

# animals = ['cow', 'cat', 'dog', 'tiger', 'lion']
# # print(*animals)
# print(animals[::1])
# animals.append('rabbit')
# print(animals[::1])

# animals.insert(0, 'elephent')
# print(animals[::1])

# nums = [1, 2, 5, 6, 10, 20, -2, 11]
# # nums.sort(reverse=True)
# # print(nums)
# # nums.reverse()
# nums.sort()
# print(nums)


# def unique(arr):
#     return list(set(arr))
#     # ans = []
#     # for i in arr:
#     #     if i not in ans:
#     #         ans.append(i)
#     #     else :
#     #         continue
#     # return ans

# print(unique([1, 2, 3, 2, 1, 3, 4, 5, 5, 4, 6]))


# '''Dictonary'''
# info = {'name':'anisul islam', 'age': 21, 'Phone': '5943312'}
# for k,v in info.items():
#     print(k, '->', v)


# def solve(*name):
#     print(f'Hi {name[0]}')


# solve('anis', 'rubel', 'siker', 'mohammad')


# a, b, c = map(int, input().split())
# print(a+b+c)

# arr = list(map(int, input('> ').split()))
# print(arr)
# print(*arr)



# nums = [1, 3, 5, 6, 9, 0]
# for num in nums:
#     if num&1:
#         print(num)
    
 
# import function
  
# print('final answer:', function.additon(10, 40))
# print('final res:', function.multiply(10, 10))
# print('final answer:', function.subtaction(100, 10))
 
 
# from function import *
 
# print('final answer:', additon(19, 10))
# print('ans:', subtaction(10, 100))
# print('res:', multiply(10, 2))

# import matplotlib.pyplot as plt
 
# labels = ('Python', 'scala', 'Java', 'C++', 'Java script', 'PHP')
# index = (1, 2, 3, 4, 5, 6)
# sizes = [45, 10, 20, 35, 42, 32]

# plt.title('Programmig Language Ugers in- 2022')
# # plt.title('Web Development')
# plt.bar(index, sizes, tick_label = labels)
# plt.ylabel('Usage')
# plt.xlabel('Programming Language')
# plt.show()

# display_person() function call
# def display_person(*args):
#     for i in args:
#         print(i)


 
 
# try:
#     age = int(input('Enter your age:'))
#     print('Your age:', age)
# except ValueError:
#     print('Invalid input!')



# try:
#     age = int(input('Enter the age:'))
#     day = age/0
#     print(day)
# except Exception:
#     print('Your can not divide 0!')
  

# class Person():
#     def __init__(self, name:str, id:int, salary:int):
#         self.name = name
#         self.id = id 
#         self.salary = salary 
    
#     def __str__(self):
#         return 'Name: {}\nId:{}\nSalary: {}'.format(self.name, self.id, self.salary)

# class Student(Person):
#     def __init__(self, name: str, id: int, salary: int, subject:str):
#         self.subject = subject
#         super().__init__(name, id, salary)
    
#     def __str__(self):
#          return 'Name: {}\nId:{}\nSalary: {}\nFavourite Subject:{}'.format(self.name, self.id, self.salary, self.subject)


# home = Person('Md Anisul islam', 314, 5000,)
# print(home)
# student = Student('Rakubul islam', 1001, 230, 'English')
# print(student)

 