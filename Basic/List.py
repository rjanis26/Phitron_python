 
# list = []

# n = int(input("Enter the sizeof list:"))
# for i in range(1, n+1):
#     data = int(input("Enter the element:"))
#     list.append(data)

# list.sort()
# print("Largest element:", list[n-1])

''' Second largest element of the list'''
# list = []

# n = int(input("Enter the sizeof list:"))
# for i in range(1, n+1):
#     data = int(input("Enter the element:"))
#     list.append(data)

# list.sort()
# print('Second largest element:', list[n-2])


'''Put even and odd element'''
  
# list = []
# n = int(input("Enter the sizeof list:"))
# for i in range(1, n+1):
#     data = int(input("Enter the element:"))
#     list.append(data)

# even = []
# odd = []

# for i in list:
#     if i&1:
#         odd.append(i)
#     else :
#         even.append(i)


# print('The even list:', even)
# print('The odd list:', odd)

''' Merge two list and sort them'''
 

# a = []
# b = []

# n = int(input("Enter the sizeof list:"))
# for i in range(1, n+1):
#     data_a = int(input("Enter the element:"))
#     a.append(data_a)

# m = int(input('Enter the sizeof list:'))
# for i in range(1, m+1):
#     data_b = int(input("Enter the element:"))
#     b.append(data_b)


# new_list = a + b
# new_list.sort()

# print('Sorted list:', new_list)


''' Sort the list length of the elements'''
 

# list = []
# n = int(input('Enter the sizeof the list:'))
# for i in range(1, n+1):
#     data = (input("Enter data:"))
#     list.append(data)

# list.sort(key=len)
# print('New list:', list)

''' Square of the number'''

# low = int(input('Enter the lower range:'))
# high = int(input('Enter the high range:'))

# ans = [(x, x**2) for x in range(low, high+1)]
# print(ans)

''' Find the prefix sum'''

# list = []
# n = int(input('Enter the sizeof the list:'))
# for i in range(1, n+1):
#     data = int(input('Enter the element:'))
#     list.append(data)

# res = [sum(list[0:i+1]) for i in range(0, len(list))]
# print('The orginal list:', list)
# print('The new list:', res)


''' Generate Random number in a list'''


# import random


# list = []
# n = int(input('Enter the sizeof the list:'))
# for i in range(n):
#     list.append(random.randint(1, 20))

# print(list)


# ''' Swap the first and last value of the list'''

# list = []
# n = int(input('Enter the sizeof the list:'))
# for i in range(0, n):
#     data = int(input('Enter the data:' + str(i+1)))

# list[0], list[n-1] = list[n-1], list[0]
# print('New list:', list)

  
# list = [1, 3, 5, 3, 5, 2, 10, 20]

# b = set()
# unique = []

# for i in list:
#     if i not in b:
#         unique.append(i)
#         b.add(i)


# print(unique)
 
# nums = []

# for i in range(3):
#     nums.append([])
#     for j in range(1, 4):
#         nums[i].append(j)
 
# print(nums)

'''list comprehention'''

# cars = ["Nissan", "Mercedes Benz", "Ferrari", "Maserati", "Jeep", "Maruti Suzuki"]
# newList = []

# for i in cars:
#     if 'M' in i:
#         newList.append(i)

# print(newList)

 

# cars = ["Nissan", "Mercedes Benz", "Ferrari", "Maserati", "Jeep", "Maruti Suzuki"]
# res = [i for i in cars if "M" in i]
# print(res)

# newList = [i for i in  range(15) if i&1]
# print(newList)


# list = [1, 3, 5, 5, 9, 10, 20]
# res = [i for i in list if i>4]
# print(res)


# a = [1, 3, 5, 6]
# b = [8, 10, 12, 22, 26]
# b.extend(a)
# print(b)

 

# country = ['Bangladesh', 'India', 'Pakistan', 'England']
# check_item = 'Australia' in country
# print(check_item) 


'''List is'''

# list1 = [200, 330, 500]
# list2 = [12, 17, 21]



# print(all(x >= 200 for x in list1))
# print(all(x >= 25 for x in list2))


# num = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(max(num, key = sum))


# num = [1, 2, 3]
# color = ['red', 'white', 'black']

# for (i, j) in zip (num, color):
#     print(i,j)



# num = [1, 3, 5 , 6, 9]

# print(*num)

# num = [1, 3, 5, 7, 9, 10]
# num2 = [2, 4, 6, 8]

# num[-1:] = num2
# print(num)


# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(list[::2])


 
# def sum(num):
#     total = 0
#     for i in num:
#         total += i
    
#     return total

# print(sum((1, 3, 5, 2)))


'''List comprehension'''
 
 
# list = [1, 2, 4, 5,6, 10]
# print('List:', [x for x in list])

# print('add:', [x+1 for x in list])
# print('subt:', [x-1 for x in list])
# print('multi:', [x*x for x in list])
# print('multi:', [x*2 for x in list])
# print('div:', [x/2 for x in list])

# list = [1, 2, 4, 8, 20, 3, 5, 8, 9, 11, 15]
# print('newlist:', [x for x in list if x > 4])
# print('newList:', [x for x in list if x> 4 if  x&1])
# print('Newlist:', [x for x in list if x> 4 if not x&1])


# a = [1, 3, 5, 6]
# b = [2, 4, 9]

# print('newList:', [[(x, y)] for x in a for y in b])

  
# list = ['0. exit', '1. addition', '2. subtraction', '3. multiplication', '4. divison']
# for i in list:
#     print(i.title()) 

# authors = ["Ernest Hemingway","Langston Hughes","Frank Herbert","Toni Morrison",
#     "Emily Dickson","Stephen King"]

# print('list:', [name[0] for name in authors])

# user_data = "Elvis Presley 987-654-3210"
# print('newlist:', [x for x in user_data if x.isdigit()])
# print('lsit:', [x for x in user_data if x.isalpha()])


'''using function list comprehension'''


# def double(x):
#     return x*2

# print('list:', [double(x) for x in range(1, 6)])

 

# sentence = "hello Bangladesh"
# print('vowels:', [i for i in sentence if i not in 'aeiou'])


'''Dictonary comprehension'''

# data = {i: i*i for i in range(1, 11)}
# print(data)

# d = {i: i*i for i in [1, 3, 5, 7]}
# print(d)


# d = {i:i+1 for i in [1, 3, 5, 7]}
# print(d)

# old_wight = {'book': 0.5, 'milk': 2.0, 'television': 7.0}
# print('new_weight:', {key: value*2.2 for (key, value) in old_wight.items()})

# ages = {'kevin': 12, 'marcus': 9, 'even':31, 'niak': 32}
# new_ages = {key:value for(key,value) in ages.items() if value> 18}
# print(new_ages)
 

# ages = {'kevin': 14, 'marcus' : 35, 'Loard' : 32, 'nicks': 34}
# new_ages = {key: value for(key, value) in ages.items() if value > 18 if not  value&1}

# print(new_ages)


# ages = {'kevin': 13, 'marcus' : 9, 'evena' : 32, 'nick': 31}
# new_ages = {key:( 'odd' if value&1 else 'even') for(key, value) in ages.items()}
# print(new_ages)
  

# names = {'Harry', 'Herminone', 'Raon', 'Neville', 'Luna'}
# index = {k:v for(k, v) in enumerate(names)}
# # print(index)


# ===================================================================================================================
#                                             List Start...
# =================================================================================================================== 

# list = [1, 2, 3, 5, 6, 9, 10]
# total = 0
# for i in list[0:len(list):2]:
#     total += i
# print(total)

# list = [i for i in range(1, 11)]
# res = sum(list[1:len(list): 2])
# ans= sum(list[0:len(list): 2])
# print(list)
# print('odd index sum:', res)
# print('even index sum:', ans)
# print('Total sum:', sum(list))

''' odd index sum from list'''

# #iterative..
# def odd_index_sum(arr):
#     total = 0
#     for i in arr[1:len(arr):2]:
#         total += i
#     return total

# print(odd_index_sum([i for i in range(1, 11)]))
# print(odd_index_sum([1, 5, 3, 10, 2]))
# print(odd_index_sum([1, 2, 4, 5, 8]))


# def odd_index_sum(arr):
#     return sum(arr[1::2])


# print(odd_index_sum([i for i in range(1, 11)]))
# print(odd_index_sum([1, 5, 3, 10, 2]))
# print(odd_index_sum([1, 2, 4, 5, 8]))

# from statistics import mode
# def most_frequent(arr):
#     return (mode(arr))
#     # frq = 0
    # res = arr[0]
    # for i in arr:
    #     curr = arr.count(i)
    #     frq = max(curr, frq)
    #     res = i
    # return res

    # return max(set(arr), key = arr.count)

# print(most_frequent([1, 2, 1, 3,3, 3,3 ,3, 3, 5, 6, 3, 1]))
# print(most_frequent([2, 3, 2, 2, 4, 1, 2,6, 7]))

# print(most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]))
# print(most_frequent([2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,2,4,6,9,1,2]))
# print(most_frequent( [1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 3]))

# def most_frequent(arr):
#     freq = 0
#     res = arr[0]
    
#     for i in arr:
#         curr = arr.count(i)
#         if curr > freq:
#             freq = curr
#             res= i
#     return res

# def is_same(a, b):
#     for x in set(a+b):
#         return False if a.count(x) != b.count(x) else True

# print(is_same([1, 2, 4], [2, 4, 1]))
# print(is_same([1, 2, 3], [1, 2, 5]))

  

# def find_weighted_avg(List, wights):
#     return sum(x*y for x, y in zip(List, wights)) / sum(wights)

# print('Abg:',round(find_weighted_avg([10, 50, 40], [2, 5, 10]),3))

# def find_weights(List, weights):
#     return sum(x*y for x, y in zip(List, weights)) / sum(weights)

# print(round(find_weights([1, 2, 4, 10], [2, 3, 5, 1]), 3))

# def weighted_average_m1(distribution, weights):
#     return round(sum([distribution[i]*weights[i] for i in range(len(distribution))])/sum(weights),2)


# def find_avg(List, weights):
#     return round(sum([List[i]*weights[i] for i in range(len(List))]) / sum(weights), 2)

# print(find_avg([10, 50, 40], [2, 5, 3]))
# print(find_avg([82, 90, 76, 83], [.2, .35, .45, 32]))

# def find_nth_min(List, n=1):
#     return sorted(List)[:n]

# print(find_nth_min([1,2,3]))
# print(find_nth_min([-2, 5, 9, 10, -1, -3, -5, 0], 3))
 

# def find_nth_max(List, n=1):
#     return sorted(List, reverse=True)[:n]

# print(find_nth_max([10, 3, 4, 5, -1, 2, 23, 24], 4))

 
# def solve(n, val = 0):
#     return [val for x in range(n)]

# print(solve(4))
# print(solve(5, 2))
# print(solve(10, 5))
 

# def difference(x, y):
#     _y  = set(y)
#     return [i for i in x if i not in _y]

# print(difference([1, 2, 4], [1, 2,3]))
# print(difference([1, 5, 6], [9,20, 1]))

 
# def find_longest(*args):
#     return max(args, key = len)

# print(find_longest('this', 'is', 'a', 'Green'))  
# print(find_longest([1, 2, 3], [1, 2], [1, 2, 3, 4, 5])) 
# print(find_longest([1, 2, 3, 4], 'Reddddddddddddd'))


# def symmetric_difference(x,y):
#     _x, _y = set(x), set(y)

#     return [i for i in x if i not in _y] + [i for i in y if i not in _x]

# print(symmetric_difference([10, 20, 30], [10, 20, 40]))
# print(symmetric_difference([1, 2, 5, 10], [-1, 3, 2, 5, 11]))

# def find_freq(List):
#     freq = {}
#     for x in List:
#         freq[x] = List.count(x)
#     return dict(freq)

# print(find_freq(['a', 'b', 'f', 'a', 'c', 'e', 'a', 'a', 'b', 'e', 'f'])) 
# print(find_freq([3,4,7,5,9,3,4,5,0,3,2,3]))


 
# def find(List, fn):
#     return next(x for x in List if fn(x))

# print(find([4, 2, 4, 5], lambda x: x&1))
# print(find([1, 20, 3, 4, 5, 6], lambda x: not x&1))


# def pluck(lst, key):
#   return [x.get(key) for x in lst]
 
# simpsons = [
#   { 'name': 'Areeba', 'age': 8 },
#   { 'name': 'Zachariah', 'age': 36 },
#   { 'name': 'Caspar', 'age': 34 },
#   { 'name': 'Presley', 'age': 10 }
# ]
# print(pluck(simpsons, 'age'))

# def convert(n):
#     return list(map(int, str(n)))

# print(convert(123))
# print(convert(1314))


class Person(object):
    def __init__(self, name, age, phone, salary):
        self.name = name 
        self.age = age 
        self.__phone = phone 
        self.salary  = salary 
    
    def __str__(self) -> str:
        return 'Name: {}, Age:{}, Phone:{}, salary:{}'.format(self.name, self.age, self.__phone, self.salary)
    


p = Person('Anisul islam', 24, '013557', 24350)
print(p) 

 





