 
 

# class String():
#     def __init__(self, string):
#         self.string  = string

#     def __repr__(self):
#         return 'String is:{}'.format(self.string)

#     def __add__(self, other):
#         return self.string + other

#     def __len__(self):
#         return len(self.string)



# if __name__ == '__main__':

#     str = String('hello wrold')
#     print(str + ' more and more')
#     print(len(str))



# class Point(object):
#     def __init__(self, x = 0, y = 0):
#         self.x = x 
#         self.y = y

#     def __str__(self):
#         return '({}, {})'.format(self.x, self.y)
    

#     # def __repr__(self):
#     #     return 'Point({}, {})'.format(self.x, self.y)
    


# p = Point(5, 10)
# print(p)

# Method overloading..
 
# class Calculator:
#     def product(self,  *args):
#         total = 1
#         for x in args:
#             total *= x 
#         print(total)
    


# cal = Calculator()
# cal.product(10,5)
# cal.product(10, 2, 2, 2)
# cal.product(100)
# cal.product(1, 2, 3, 4, 5, 2)

# class Data:
#     def __init__(self, x):
#         self.x = x 
    

#     def __lt__(self, other):
#         if self.x < other.x:
#             return 'Num_1 is big'
#         else:
#             return 'Num_2 is big'


# data = Data(10)
# print(data, 100)

 

# class SoftwareEngineer:
#     def __init__(self, name, age, role, salary):
#         self.name = name
#         self.age = age 
#         self.role = role 
#         self.salary = salary


#     def __str__(self):
#         return 'Name:{}\nAge:{}\nRole:{}\nSalary:{}'.format(self.name, self.age, self.role, self.salary)
     

# sf = SoftwareEngineer('Anisul islam', 23, 'Software Testing', 2432525)
# st = SoftwareEngineer('Rakin islam', 32, 'Debugging the Test', 2113098)
# print(sf)
# print(st)

'''Encapsulation'''
 
 

# class Student:
#     def __init__(self, name, id):
#         self.__name = name 
#         self.__id = id 
    
#     def details(self):
#         print('Name: {}\nId:{}'.format(self.__name, self.__id))
    
#     def set_id(self, id):
#         if id > 0 :
#             self.__id = id 
#         else:
#             print('OOPS! invlid id')
    
#     def get_id(self):
#         return self.__id 

#     def set_name(self, new_name):
#         if new_name.isalpha():
#             self.__name = new_name
#         else:
#             print('opps! invalid input for name.')


#     def get_name(self):
#         return self.__name


# s1 = Student('Rakibul', 324)
# s2 = Student('Catrol', 544)
# # s1.update_id(-342)
# # s1.set_id(39)
# # print(s1.get_id())
# # print(s1.get_id())


# s1.set_name('Rasul islam')
# print(s1.get_name())
# s1.details()
 

# class Person:
#     def __init__(self, first, last, add):
#         self.first = first 
#         self.last = last 
#         self.address = add 
    

#     @property
#     def email(self):
#         return self.first + '.'+self.last+'@gmail.com'
    
#     @property
#     def full_name(self):
#         return '{} {}'.format(self.first, self.last)
    

#     @full_name.setter
#     def full_name(self, new_name):
#         self.first, self.last = new_name.split()
    


# p = Person('Sam', 'Edison', 'Bangladesh')
# print(p.full_name)
# print(p.email)

# # p.first = 'Ratul'
# # print(p.email)
# # print(p.full_name)

# p.full_name = 'Rialee Rosow'
# print(p.full_name)
# print(p.email)


# class Student:
#     def __init__(self, total):
#         self._total = total
    

#     def average(self):
#         return self._total/5.0
     
#     @property
#     def total(self):
#         return self._total
    
#     @total.setter
#     def total(self, t):
#         if t < 0 or t > 500:
#             print('invalid input.')
#         else:
#             self._total = t


# res = Student(450)
# print(res.total)
# print(res.average())

# res.total = 100 
# print(res.total)
# print(res.average())
 

# class Employee:
#     def __init__(self, position = None):
#         self._position = position
    
#     @property
#     def position(self):
#         return self._position


#     @position.setter
#     def set_position(self, pos):
#         if pos is not None and len(pos) <= 2:
#             raise ValueError('position name is less than 2')
#         self._position = pos 
    

# em = Employee('entry')
# bm = Employee('Entry')
# print(em.position)
# em.position = 'os'
# bm.position = 'Senior'

# print(em.position)
# print(bm.position)
 
 