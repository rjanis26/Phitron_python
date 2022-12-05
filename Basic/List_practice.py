 
# def find_max(list):
#     return max(list)

# print(find_max([1, 3, 5, -1, 20, 3]))
# print(find_max([13, 10, 2, 34]))


# def findmax(list):
#     max = list[0]
#     for i in list:
#         if i > max:
#             max = i
#     return max


# print(findmax([1, 3, 10, 20, 1]))
# print(findmax([1, 21, -1]))
 
# def find_smallest(list):
#     min = list[0]
#     for i in list:
#         if i< min:
#             min = i
#     return min
#     # return min(list)

# print(find_smallest([1, 0, 19, 20, -1, -20]))
# print(find_smallest([10, 20, 0, 23, 20]))


# def match_words(string):
#     count = 0
#     for str in string:
#         if len(str) > 1 and str[0] == str[-1]:
#             count += 1
    
#     return count

# print(match_words(['abc', 'xyz', 'aba', '121', 'geeg']))
# print(match_words(['535', 'wrods', 'lo']))

# def last(n):
#     return n[-1]

# def sorted_list(tup):
#     return sorted(tup, key = last)

 
# print(sorted_list([(2, 5), (1, 2), (4, 5)]))

 

# def find_unq(list):
#     unique = set()
#     for i in list:
#         unique.add(i)
#     return unique


# print(find_unq([10,20,30,20,10,50,60,40,80,50,40]))

  
# def removeDuplicate(list):
#     stack = []
#     for i in range(len(list)):
#         if len(stack) == 0 or stack[-1] != list[i]:
#             stack.append(list[i])
#         else:
#             stack.pop()
    

#     ans = []
#     while(len(stack)):
#         ans += stack[-1]
#         stack.pop()
    
#     ans.reverse()
#     return ans


# print(removeDuplicate([10,20,30,20,10,50,60,40,80,50,40]))


'''Remove duplicate from list'''

# def remove_duplicate(arr):
#     # return list(set(arr))
#     # return list(dict.fromkeys(arr))

# print(remove_duplicate([1, 1, 2,3 , 5, 6, 1, 5, 6]))
# print(remove_duplicate([1, 2, 1, 2, 3]))


# def is_empty(list):
#     return True if len(list) == 0 else False
#     # return True if not list else False

# print(is_empty([1,3, 5,6]))
# print(is_empty([]))
 

# def long_wrods_count(n, str):
#     res = []
#     for word in str.split(' '):
#         if len(word) > n:
#             res.append(word)
#     return res

# print(long_wrods_count(3, 'the quick brown fox jumps over the lazy dog'))


# def common_data(a, b):
#     res = False;
#     for i in a:
#         for j in b:
#             if i == j:
#                 res = True
#                 return res

# print(common_data([1,2,3,4,5], [5,6,7,8,9]))
# print(common_data([1,2,3,4,5], [6,7,8,9]))


# def common_data(a, b):
#     for x in b:
#         for x in a:
#             return True
#     return False

# print(common_data([10, 20, 30, 40, 50, 60], [22, 42]))
# print(common_data([10, 20, 30, 40, 50, 60], [20, 80]))


# color = ['red', 'green', 'white', 'black', 'pink', 'yellow']
# print([x for i, x in enumerate(color) if  i&1])


# nums = [7, 8, 120, 25, 44, 20, 27]
# print([x for x in nums if x&1])


# def solve():
#     res = [x*x for x in range(1, 21)]
#     print(res[:5])
#     print(res[-5:])
 
# solve()

# def print_values():
#     ans = [x*x for x in range(1, 31) if x&1]
#     print(ans[5:])

# print_values()

 
# import itertools
# def find_permutations(arr):
#     return list(itertools.permutations(arr))

# print(find_permutations([1, 2, 4]))
# print(find_permutations([1, 3,  6]))


# nums = [5, 15, 35, 8, 98]
# for index , val in enumerate(nums):
#     print(index, val)


# str = ['a', 'b', 'c', 'd']
# print(''.join(str))


# num = [10, 20, 30, 5, -8]
# print(num.index(20))


# import itertools
# lst = [[1, 2, 5], [4, 6,5],[9], [10, 11, 20]]
# print(list(itertools.chain(*lst)))
 
# def flatten(nums):
#     return [x for y in nums for x in y]

# print(flatten([[1, 2, 3, 5], [6, 7, 9], [10]]))


# nums = [1, 3, 5, 2]
# color = ['red', 'green', 'black']
# # print(nums+color)
# # nums.extend(color)
# # print(nums) 


# for i in color:
#     nums.append(i)

# print(nums)

 
# import random
# color_list = ['red', 'green', 'blue', 'white','black']
# print(random.choice(color_list))

'''find second smallest in list'''

# def second_smallest(arr):
#     if len(arr) < 2:    #base case...
#         return 
#     if len(arr) == 2 and arr[0] == arr[1]:
#         return
    
#     first = second = arr[0]
#     for i in range(len(arr)):
#         if first > arr[i]:
#             first = arr[i]
    
#     for i in range(len(arr)):
#         if second > arr[i] and first != arr[i]:
#             second = arr[i]
        
#     return second

# print(second_smallest([1, 2, -8, -2, 0, -2]))
# print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
# print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# print(second_smallest([2,2]))
# print(second_smallest([2]))


# def second_largest(arr):
#     # if len(arr) < 2:
#     #     return 
#     # if len(arr) == 2 and arr[0] == arr[1]:
#     #     return 
    
#     first = second = arr[0]
#     for i in range(len(arr)):
#         if i < first:
#             first = arr[i]
    
#     for i in range(len(arr)):
#         if second < arr[i] and first != arr[i]:
#             second = arr[i]
    
#     return second


# print(second_largest([1,2,3,4,4]))
# print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# print(second_largest([2,2]))
# print(second_largest([1]))


# def second_largest(arr):
#     arr.sort()
#     return arr[-2]


# print(second_largest([1,2,3,4,4]))
# print(second_largest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
# print(second_largest([2,2]))
# print(second_largest([1]))
 

# def solve(arr):
#     return list(dict.fromkeys(arr))
#     # return list(set(arr))

# print(solve([10, 20, 30, 40, 20, 50, 60, 40]))


'''find frequencey all of list value'''
  
# list = [1, 3, 5, 2, 2, 1,3 ]
# counter = {}

# for i in list:
#     if i in counter:
#         counter[i] += 1
#     else:
#         counter[i] = 1

# print(counter)

# def count_frequencey(arr):
#     freq = {}
#     for i in arr:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1
#     return(freq)

# print(count_frequencey([10, 20, 30, 40, 20, 50, 60, 40]))


  
# def count_freq(list):
#     freq = {}
#     for items in list:
#         freq[items] = list.count(items)
#     return freq

# print(count_freq(['a', 's', 'a', 's', 'c', 'c', 'c','b']))

 

'''find the freq in list items'''
# def count_freq(list):
#     freq = {}
#     for item in list:
#         freq[item] = list.count(item)
#     return freq
 

# arr = []
# n = int(input('enter the n:'))
# for i in range(1, n+1):
#     data = int(input('Enter the data:'))
#     arr.append(data)

# for k, v in count_freq(arr).items():
#     print(k,'->', v)



#another way....
 

# def count_freq(list):
#     freq = {}
#     for i in list:
#         freq[i] = freq.get(i, 0)+1
#     return freq

# print(count_freq(['a', 'a', 1, 1, 1, 'b', 'b', 'b', 2, 2, 2]))


'''count the unique element from list'''
 
 
# def count_unique(arr):
#     return len(list(set(arr)))

# print(count_unique( [10, 20, 30, 50, 80, 70, 70, 80, 10]))

#iterative solutions::

# def count_unique(arr):
#     count = 0;
#     list = []
#     for i in arr:
#         if i not in list:
#             count += 1
#             list.append(i)
#     return count
     
# print(count_unique( [10, 20, 30, 50, 80, 70, 70, 80, 10]))

# def find_product_unique(arr):
#     total = 1
#     for i in list(set(arr)):
#         total *= i
#     return total

# print(list(set([2,1,2,4,6,4,3,2,1])))
# print(find_product_unique([2,1,2,4,6,4,3,2,1]))
 

# def solve(arr, k):
#     res = []
#     for i in arr:
#         freq = arr.count(i)
#         if freq > k and i not in res:
#             res.append(i)
#     return res

# print(solve( [4, 6, 4, 3, 3, 4, 3, 7, 8, 8], 2))


# def three_consecutive(arr):
#     for i in range(len(arr)-2):
#         if arr[i] == arr[i+1] and arr[i+1] == arr[i+2]:
#             print(arr[i])
 
# three_consecutive([18, 18, 18, 6, 3, 4, 9, 9, 9])


# val = ['Tutor', 'joes', 'computer', 'education']
# print('Orgianl list:', val)
# print(val[::-1])


# val = ['p', 'Y', 'T', 'H', 'o', 'N']
# print('Orginal list:' + str(val))

# ans = [i if i == 'T' else '@' for i in val]
# print(ans)


 
# val  = ['TutorJoes','ComputerEducations']
# res = []
# for i in val:
#     t= [[]]
#     for ch in i:
#         if ch.isupper():
#             t.append([])
#         t[-1].append(ch)
#     res.append(' '.join(''.join(i) for i in t))

# print(res)


# def isHas(a, b):
#     return True if a in b else False

# print(isHas('Phi', 'Phitron')) 
 


# def is_palindrome(n):
#     return True if str(n) == str(n)[::-1] else False

# print(is_palindrome(121))
# print(is_palindrome(1312))


# def reveser_string(n):
#     return str(n)[::-1]

# print(reveser_string(76542))
 
# def count_inList(arr, first, last):
#     count = 0
#     for x in arr:
#         if first <= x <=last:
#             count += 1
#     return count


# print(count_inList( [10,20,30,40,40,40,70,80,99], 40, 100))
# print(count_inList(['a', 'b', 'c', 'd', 'e', 'f'], 'a', 'e'))


'''Sieve of Eratosthenes'''
 

# def is_prime(n):
#     prime = []
#     for i in range(2, n+1):
#         if i not in prime:
#             prime(i)
#         for j in range(i*i, n+1, i):
#             prime.append(j)
     
# # n = int(input())
# # print(is_prime(n))
# print(is_prime(10))

# def prime_eratosthenes(n):
#     prime_list = []
#     for i in range(2, n+1):
#         if i not in prime_list:
#             print (i)
#             for j in range(i*i, n+1, i):
#                 prime_list.append(j)


# print(prime_eratosthenes(5), end=' ')


# list = [11, 33, 50]
# print(list)
# ans = int(''.join(map(str, list)))
# print(ans)
  

# def remove_items(arr, n):
#     count = 0
#     res = []
#     for x in arr:
#         if count > n or not x%2 == 0:
#             res.append(x)
#         else:
#             count += 1
#     return res

# nums = [3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]
# n = 2
# print(remove_items(nums, n))
  

# def remove_fist_element(list):
#     # list.remove(list[0])
#     # return list
#     # list.pop(0)
#     # return list
#     # del list[0]
#     # return list
#     # return list[1:]

# print('Orgirnal list:')
# print(['hello', 'btech', 'geeks', 'is', 'new', 'online'])
# print(remove_fist_element(['hello', 'btech', 'geeks', 'is', 'new', 'online']))
# print(remove_fist_element([1, 3, 5, 8, 9, 10]))


# def remove_last_element(list):

#     # del list[-1]
#     # return list
#     # list.pop()
#     # return list
#     # return arr[:-1]


# print(['hello', 'btech', 'geeks', 'is', 'new', 'online'])
# print(remove_last_element(['hello', 'btech', 'geeks', 'is', 'new', 'online']))
# print(remove_last_element([1, 3, 5, 8, 9, 10]))
 


'''Little bit advanced problem'''
 
# def solution(arr):
#     res = []
#     for i, x in enumerate(sorted(arr)):
#         for y in arr[i+1:]:
#             if y-x == 3:
#                 res.append([x, y])
#     return res


# n = int(input('Enter the n:'))
# arr = []
# for i in range(1, n+1):
#     data = int(input('Enter the data:'))
#     arr.append(data)

# print(solution(ar
 

# first_name = input('Enter your first name:')
# second_name = input('Enter your second name:')

# full_name = f'{first_name} {second_name}'

# print('Your full name is:', full_name)
# print('Your format name is:', full_name.title())
# print('Your Upper case name:', full_name.upper())

# change_second_name = input('Replace your second name:')
# new_full_name = full_name.replace(second_name, change_second_name)

# print(full_name, 'Your new name is:', new_full_name)
 

# def solve(arr):
#     res = []
#     for i, x in enumerate(sorted(arr)):
#         for y in arr[i+1:]:
#             if y-x == 3:
#                 res.append([x, y])
#     return res

# print(solve([0, 3, 4, 7, 9]))


# def solve(arr):
#     return [[x, x+3] for x in arr if x+3 in arr]

# print(solve([x for x in range(1,6)]))
 

# def solve(str, n):
#     res = ''
#     for i in str:
#         if i in 'aioueAEIOU':
#             res += i
#     return res[:n] if len(str) >= n else 'n is less than number of vowels present in the string.'


# # print(solve('python exercise', 3))
# str = input('Enter the string:')
# n = int(input('Enter the n:'))

# print(solve(str, n))

 
# def solve(str, n):
#     res = [x for x in str if x in 'aeiouAEIOU']
#     return 'n is less than num' if len(res) < n else ''.join(res[:n])

# print(solve('python exercise', 5))


# def solve(arr):
#     return all([is_prime(i) for i in arr])
#     # return all(is_prime(i) for i in arr)

# def is_prime(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return True
#     else:
#         for x in range(2, n):
#             if n % x == 0:
#                 return False
#         return True

# print(solve([ 3, 5, 7, 9]))
# print(solve([3, 5, 7, 13]))
# print(solve([0, 3, 4, 7, 9]))

# def solve(arr):
#     mx = max(arr)
#     mn = min(arr)
#     return sum(range(mn, mx+1)) - sum(arr)

# print(solve([0, 3, 4, 7, 9]))
 

# def find_missing(arr):
#     res = len(arr)
#     for i in range(len(arr)):
#         res += (i - arr[i])
#     return res

# def find_sum_missing(arr):
#     return sum(range(min(arr), max(arr)+1)) - sum(arr)

# print(find_sum_missing([0, 3, 4, 7, 9]))


# def solve(nums):
#     nums.sort()
#     return max([sorted(nums)[i]-sorted(nums)[i-1]  for i in range(1,len(nums))]), min([sorted(nums)[i]-sorted(nums)[i-1]  for i in range(1,len(nums))])    

# print(solve([0, 9, 2, 4, 5, 6]))

# def find_odd(arr):
#     odd_max = [x for x in arr if x&1]
#     return -1 if len(odd_max) == 0 else max(odd_max)

# print(find_odd([0, 9, 2, 4, 5, 6]))
# print(find_odd([x for x in range(1,11)]))


# def find_odd(arr):
#     ans = -1
#     for x in arr:
#         if x&1 and x > ans:
#             ans = x
#     return ans

# print(find_odd([-4, 0, 6, 1, 0, 2]))

# def find_oddMax(arr):
#     odd = [x for x in arr if x&1]
#     return -1 if len(odd) == 0 else max(odd)

# print(find_oddMax([0, 9, 2, 4, 5, 6]))
# print(find_oddMax([1,3, 2]))

#iterative

# def find_odd_max(arr):
#     ans = -1
#     for x in arr:
#         if x&1 and x > ans:
#             ans = x 
#     return ans


# print(find_odd_max([0, 9, 2, 4, 5, 6]))
# print(find_odd_max([1,3, 2]))

# def current_sum(arr):
#     return [sum(arr)-(x) for x in arr]

# print(current_sum([0, 9, 2, 4, 5, 6]))
# print(current_sum([x for x in range(1, 6) if x&1]))

 

# def count_lower(str):
#     return sum([el.islower() for word in str for el in word])

# print('Total lower:', count_lower(['Red', 'Green', 'Blue', 'White']))
# print('Total lower:', count_lower(['SQL', 'C++', 'C','PHP']))

import imp
from itertools import count
from msilib import sequence
from shutil import move
from this import d


# def count_lower(string):
#     return sum(map(str.islower, str(string)))

# print('Total:', count_lower('hello wolD'))


# def has_duplicate(arr):
#     return len(arr) != len(set(arr))

# print(has_duplicate([x for x in range(1, 8)]))
# print(has_duplicate([1, 3, 2, 2, 2, 1, 3]))
# print(has_duplicate([1, 2, 3, 6]))


# def is_contained_in(a,b):
#     for x in set(a):
#         return False if a.count(x) > b.count(x) else True

# print(is_contained_in([1, 2], [2, 4, 1]))
# print(is_contained_in([1], [2, 4, 1]))
# print(is_contained_in([1, 1], [4, 2, 1]))
# print(is_contained_in([1, 1], [3, 2, 4, 1, 5, 1]))

#another way..

# def is_contained_in(a, b):
#     return len(set(a).intersection(b)) > 0
#     # return any(map(lambda x: x in b, a))
#     # return True if set(a) & set(b) else False
#     # return set(b).issubset(set(b))
#     # return any(x in b for x in b)
#     # return True if any(x in a for x in b) else False 
#     # return (set(a).issubset(set(b)))
#     # return all([x in b for x in a])


# print(is_contained_in([1, 2], [2, 4, 1]))
# print(is_contained_in([1], [2, 4, 1]))
# print(is_contained_in([1, 1], [4, 2, 1]))
# print(is_contained_in([1, 1], [3, 2, 4, 1, 5, 1]))


# def nth_element(n, arr):
#     return arr[n]

# # print(nth_element(2, [1,2,4, 5]))
# # print(nth_element(1, [x for x in range(1,6)]))
# print(nth_element(2, []))


# def every_nth(nums, n):
#     return nums[n-1::n]
#     # return nums[n]

# print(every_nth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
# print(every_nth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))
# print(every_nth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
# print(every_nth([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6))


# from itertools import accumulate
# def find_preSum(arr):
#     return list(accumulate(arr))

# print(find_preSum([x for x in range(1, 5)]))
# print(find_preSum([-1, -2, -3, 4]))


# def find_preSum(arr):
#     res = []
#     sum = 0
#     for i in range(0, len(arr)):
#         sum += arr[i]
#         res.append(sum)
#     return res

# print(find_preSum([10, 20, 30, 30, 50]))

# def find_preSum(lists):
#     res = [sum(lists[0:x:1]) for x in range(0, len(lists)+1)]
#     return res[1:]

# print(find_preSum([10, 20, 30, 30, 50]))


# def find_pre_sum(arr):
#     res =  [sum(arr[0:x:1]) for x in range(0, len(arr)+1)]
#     return res[1:]
# print(find_pre_sum([10, 20, 30, 40, 50]))

# def cast_list(val):
#     return list(val) if isinstance(val, tuple, list, set, dict) else [val]

# print(cast_list([1]))


# def fibonacci_nums(n):
#     if n <= 0: 
#         return [0]
#     sequence = [0, 1]
#     while len(sequence) <= n:
#         val = sequence[len(sequence)-1] + sequence[len(sequence)-2]
#         sequence.append(val)
#     return sequence

# print(fibonacci_nums(5))
# print(fibonacci_nums(7))


'''fibonacci series using recursion'''
# def fibonacci(n):
#     if n<0:
#         print('opps! invalid input')
#     elif n == 0: return 0
#     elif n == 1 or n == 2: return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# n = int(input('> '))
# print(fibonacci(n))


# #another way....
# def fibonacci(n):
#     if n <= 0: return [0]
#     fib_list = [0, 1]
#     while len(fib_list) <= n:
#         val = fib_list[len(fib_list) -1 ] + fib_list[len(fib_list) -2]
#         fib_list.append(val)
#     return fib_list


# while True:
#     n = int(input('> '))
#     if n == 0: break
#     print(fibonacci(n))

# def move_end(arr, n):
#     return arr[n:] + arr[:n]


# print(move_end([1, 2, 3, 5, 6], 4))


# def most_frequent(arr):
#     return max(set(arr), key = arr.count)

# print(most_frequent([1, 2, 2, 2, 3, 3, 3,3, 5]))
# print(most_frequent([1, 1, 1, 2, 2, 3, 3]))


#Naive solution...

# def most_frequent(arr):
#     freq = 0
#     res = arr[0]
    
#     for i in arr:
#         curr = arr.count(i)
#         if curr > freq:
#             freq = curr
#             res= i
#     return res

# print(most_frequent([2,1 , 2,2, 2, 1, 3]))
# print(most_frequent([1, 2, 3, 4]))

# from statistics import mode
# def most(List):
#     return (mode(List))

# print(most([2, 1, 2, 2, 1, 3]))

# def is_same(a, b):
#     for x in set(a+b):
#         return False if a.count(x) != b.count(x) else True

# print(is_same([1,2,4], [2, 4, 1]))

# print('Hello world')

 