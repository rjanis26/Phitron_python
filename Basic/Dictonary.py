 
# key = int(input('Enter the key:'))
# val = int(input('Enter the value:'))

# dict = {}
# dict.update({key:val})
# print(dict)

 


# n = int(input('Enter the n:'))
# d = {i: i*i for i in range(1, n+1) if not i&1}
# print(d)


# d = {'a': 100, 'b':200, 'c': 300}
# print('sum of dict:', sum(d.values()))
 

# d = {'a':5, 'b' : 10, 'c':10}
# total = 1

# for i in d:
#     total *= d[i]

# print(total)



# d = {'a': 1, 'b': 2, 'c': 3 }
# print(d)

# key = input('Enter the key to delete:')
# # if key in d:
#     del d[key]

# else :
#     print('key not found!')
#     exit(0)

# print('New dict:', d)

''' Basic problem solving in python'''

# d  = {i:i for i in range(1, 11) if i&1}
# print(d)
# print(sorted(d.items(), reverse=True))

 

# people = {3: 'Jim', 2:'jack', 4:'Jane', 1:'Jill'}
# # print(dict(sorted(people.items(), reverse=True)))

# print(dict(sorted(people.items(), key = lambda item : item[1])))

# d = {0:10, 1:20}
# print(d)
# d.update({2:30})
# print(d)


# for k, v in d.items():
#     print(k,'->', v)


# d1 = {1:10, 2: 20}
# d2 = {3:30, 4: 40}
# d3  = {5: 50, 6: 60}
# res = {}
# for d  in (d1, d2, d3):
#     res.update(d)
# print(res)


# def is_present(k, d):
#     return True if k in d else False

# print(is_present(5, {1: 10, 2: 20, 3:40, 5:50, 6: 100}))
# print(is_present(4, {i:i for i in range(1,6) if not i&1}))

# d = {'x': 10, 'y':20, 'z': 300}
# for k, v in d.items():
#     print(k, '->', v)

# def helper(n):
#     return  {i:i*i for i in range(1, n+1)}

# n = int(input('enter the n:'))
# print(helper(n))


# print({i:i*i for i in range(1, 16)})
 

# d1, d2 = {'a': 100, 'b': 200}, {'x':300, 'y': 400}
# # res = d1.copy()
# # res.update(d2)
# # print(res)

# res = {}
# for d in (d1, d2):
#     res.update(d)
# print(res)


# d = {'data1': 100, 'data2': -54, 'data3':247}

# print(sum(d.values()))

# d = {'data1': 100, 'data2': -54, 'data3': 247}
# res = 1
# for k in d:
#     res *= d[k]
# print(res)

# my_dict = {'a':1, 'b':2, 'c':3, 'd':5}
# print(my_dict)
# if 'a' in my_dict:
#     del my_dict['a']
# print(my_dict)


# key = {'red', 'green', 'blue'}
# val = {'#ff000', '#000400', '#0000FFF'}

# # print(dict(zip(key, val)))

# def sort_dict(d, reverse = False):
#     return dict(sorted(d.items(), reverse=reverse))

# print(sort_dict({ 'name1': 'Theodore', 'name2': 'Mathew', 'name4': 'Roxanne', 'name3': 'David' }))
# print(sort_dict({ 'name1': 'Theodore', 'name2': 'Mathew', 'name4': 'Roxanne', 'name3': 'David' }, True))

 

# def get_min(d):
#     return max(d.keys(), key = (lambda k: d[k]))
#     # return min(d.keys(), key = (lambda k: d[k]))


# d = {'x':500, 'y':-500, 'z':1000}
# print(d[get_min(d)])

 

# n = int(input('Enter the value:'))
# d = {}
# for i in range(1,n+1):
#     key = int(input('Enter key:'))
#     value = input('Enter the value:')
#     d[key] = value
# print(d)
 

# n = int(input('Enter the n:'))
# d = {}
# for i in range(1, n+1):
#     k = int(input('Enter the key:'))
#     v = input('Enter the value:')
#     d.update({k:v})

# print(d)
 

# class dictobj(object):
#     def __init__(self):
#         self.x = 'red'
#         self.y = 'yellow'
#         self.z = 'green'
#     def do_nothng(self):
#         pass

# test = dictobj()
# print(test.__dict__)

'''Romove duplicate from dictornary...'''

# def remove_duplicate(d):
#     temp = {val:key for key, val in d.items()}
#     return {v:k for k,v in temp.items()}
#     # res = {}
#     # for k, v in d.items():
#     #     if v not in res.values():
#     #         res[k] = v
#     # return res


# n = int(input('Enter the n:'))
# d = {}
# for i in range(1, n+1):
#     k = int(input('Enter the k:'))
#     v = input('Enter the value:')
#     d.update({k:v})

# print(remove_duplicate(d))


# def is_empty(d):
#     return True if len(d) == 0 else False
#     # return not bool(d)

# print(is_empty({}))
# print(is_empty({1:10, 2:20, 3:20}))


# def print_unique(dic):
#     return set(val for d in dic for val in dic.values())

# print(print_unique ([{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]))

# from heapq import nlargest
# d = {'a':500, 'b': 5760, 'c': 560, 'd':400, 'e':1500, 'f':500}
# res = nlargest(3, d, key = d.get())
  

# a, b, c = map(int, input("enter the three num:").split())
# largest = a

# if b > largest:
#     largest = b
# elif c > largest:
#     largest = c

# print('Lagest value:', largest)
 
# from heapq import nlargest
# d = {'a': 500, 'b':5874, 'c': 560, 'd': 400, 'e': 576}
# three_largst = nlargest(3, d, key=d.get))
 

# from collections import defaultdict, Counter
# str = 'w3resource'

# d = {}

# for letter in str:
#     d[letter] = d.get(letter, 0)+1
# print(d)

# str = input('Enter the string:')
# dic = {}
# for s in str:
#     dic[s] = dic.get(s, 0)+1
# print(dic)

# student = [ {'id':1, 'success': True, 'name': 'Lary'},
#             {'id':2, 'success':False, 'name':'Rabi'},
#             {'id':3, 'success': True,'name': 'Alex'}

#         ]

# print(sum(d['id'] for d in student))
# print(sum(d['success'] for d in student))
  
# def sort_dic(dic):
#     return {x: sorted(y) for x, y in dic.items()}

# print(sort_dic({'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}))

# student = {'s 001': ['Math', 'Science'], 's   0002':['Math', 'English'] }
# ans = {x.translate({32: None}): y for x, y in student.items()}
# res = {x.translate({32:None}) : y for x, y in student.items()}
# print(res)
# print(ans)

 
# from heapq import nlargest
# from operator import itemgetter

# dic = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# for k,v in nlargest(4, dic.items(), key = itemgetter(1)):
#     print(k, v)



# dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# print('Key  Value  Count')
# for count, (k,v) in enumerate(dic.items(), 1):
#     print(k, '  ', v, '     ', count)
 


# students = {'Aex':{'class':'V',
#         'rolld_id':2},
#         'Puja':{'class':'V',
#         'roll_id':3}}

# for a in students:
#     print(a)
#     for b in students[a]:
#         print(b, ':', students[a][b])


# def count_items(dic):
#     return (sum(map(len, dic.values())))


# print(count_items({'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}))

# def create_string(List):
#     return ''.join(List)

# print(['This', 'is', 'very', 'fanstastic'])

# str = ['This', 'is', 'very', 'fanstastic']
# print(' '.join(str))

# def solve(List):
#     for x in List:
#         print(x, end=' ')

# # print(solve(['Hello', 'Man', 'How', 'are', 'you']))

# solve(['Hello', 'Man', 'How', 'are', 'you'])


# List =  ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

# str = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
# res_str = str.split(' ');

# for i in range(1,len(List)+1):
#     ele = res_str[i]
#     if not i&1:
#         for j in range(1, len(res_str)+1):
#             ble = res_str[j]
#             if(ele == ble):
#                 res_str[j] = res_str[i+1]


# print(' '.join(res_str))
 
''' find min key from dict...'''
 

# def find_min(d):
#     return max(d, key=d.get), min(d, key=d.get)


# students = {'Theodore': 50, 'Roxanne': 22, 'Mathew': 32, 'Betty': 20};
# print(find_min(students))
 

# def solve(Dict):
#     return list(Dict.values()) 

# students = {'Theodore': 50, 'Roxanne': 22, 'Mathew': 32, 'Betty': 20};
# # print(solve(students))
# ans =solve(students)
# print(max(ans))
# print(min(ans)) 
# print(sum(ans))

# def solve(Dict):
#     return list(Dict.keys())

# students = {'Theodore': 50, 'Roxanne': 22, 'Mathew': 32, 'Betty': 20};
# print(solve(students))
# ans = solve(students)
# print([x for x in ans])
# for i in ans:
#     print(i)

# ans.sort()
# print(ans)

# def solve(d):
#     ans = []
#     for x, y in d.items():
#         ans.extend([x, y])
#     return ans

#     # return list(d.items())

# d = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}
# print(solve(d))

# def solve(k, v):
#     return dict(zip(k, v))

# l1 = ['a', 'b', 'c', 'd', 'e', 'f']
# l2 = [1, 2, 3, 4, 5]     

# print(solve(l1, l2))

  
# def solve(d, val):
#     return list(k for k, v in d.items() if v == val)


# students = {'Theodore': 50, 'Roxanne': 20, 'Mathew': 32, 'Betty': 20};
# print(solve(students, 20))


# def solve(d):
#     return {value: key for key, value in d.items()}

# students = {
#   'Theodore': 10,
#   'Mathew': 11,
#   'Roxanne': 9,
# }

# print(solve(students))


# def solve(List, fn):
#     return dict(zip(List, map(fn, List)))


# print(solve([x for x in range(1, 11) if not x&1], lambda x: x*x))


# def solve(d, k, v):
#     return True if any(sub[k] == v for sub in d) else False


# students = [
#         {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
#         {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
#         {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
#         {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
#         {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
#         ]


# print(solve(students, 'student_id', 2)) 

# def solve(dict, kes):
#     return [list(d[k] for  k in keys) for d in dict]


# students = [
#         {'student_id': 1, 'name': 'Jean Castro', 'class': 'V'}, 
#         {'student_id': 2, 'name': 'Lula Powell', 'class': 'V'},
#         {'student_id': 3, 'name': 'Brian Howell', 'class': 'VI'}, 
#         {'student_id': 4, 'name': 'Lynne Foster', 'class': 'VI'}, 
#         {'student_id': 5, 'name': 'Zachary Simon', 'class': 'VII'}
#         ]

# print(solve(students,('student_id', 'name', 'class')))

# from collections import Counter
# def freq(d):
#     return Counter(d.values())


# dictt = {'V':10, 'VI':10, 'VII':10, 'VIII':20, 'IX': 70, 'X':80, 'XI':80, 'XII':100}
# # # print(freq(dictt))
# # ans = freq(dictt)

# # for k, v in ans.items():
# #     print(k,'->',v)

# for k, v in (freq(dictt)).items():
#     print(k, '->', v)

# def solve(dictt):
#     return [k for k,v in dictt.items() if len(v)== 1]


# dictt = {
#  'V': [10, 12],
#  'VI': [10],
#  'VII': [10, 20, 30, 40],
#  'VIII': [20],
#  'IX': [10,30,50,70],
#  'X': [80]
#  }

# print(solve(dictt))

# def solve(d, N):
#     return sorted(d, key=d.get, reverse=True)[:N]

# dictt = {'a':5, 'b':14, 'c': 32, 'd':35, 'e':24, 'f': 100, 'g':57, 'h':8, 'i': 100}
# print(solve(dictt, 3))

# def solve(d):
#     return {key:[x for x in val if not x&1] for key, val in d.items()}


# students = {'V' : [1, 4, 6, 10], 'VI' : [1, 4, 12], 'VII' : [1, 3, 8]} 

# # print(solve(students))
# ans = solve(students)
# for k,v in ans.items():
#     print(k, '->', v)


# def solve(d):
#     return list(map(list, d.items()))

# color_dict = {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
# print(solve(color_dict))


# def solve(d):
#     res = {}
#     for val in d.values():
#         res[val] = len(val)
#     return res 

# color_dict = {1 : 'red', 2 : 'green', 3 : 'black', 4 : 'white', 5 : 'black'}
# ans = solve(color_dict)
# for k, v in ans.items():
#     print(k, '-> Len:', v)


# def solve(d):
#     res = {}
#     for val in d.values():
#         res[val] = len(val)
#     return res 

# color_dict = {1 : 'red', 2 : 'greens', 3 : 'black', 4 : 'white', 5 : 'black'}
# ans = solve(color_dict)
# for k, v in ans.items():
#     print(k, '->Len: ', v) 

