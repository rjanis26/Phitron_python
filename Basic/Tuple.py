# ''' First program '''
# tp =  5, 10, 15, 20, 25
# print(tp)
# tp = 5,
# print(tp)

'''convert a tuple to string'''

# tup = ('w','3', 's', 'c', 'h','o', 'o', 'l')
# str = ''.join(tup)
# print(str)


'''Find the items'''

# tup = 2, 4, 5, 6, 8, 9, 10,5, 6, 5, 5, 5
# print(tup)

# count = tup.count(5)
# print('item has:', count,'times')


''' append, delete, display of a list using classes'''
  
# class check():
#     def __init__(self):
#         self.n = []
    
#     def add(self, data):
#         return self.n.append(data)
    
#     def remove(self, b):
#         self.n.remove(b)
    
#     def display(self):
#         return self.n
    

# ch = check()

# choose = 1

# while choose != 0:
#     list = ['0. Exit', '1. Add', '2. delete', '3.display']
#     for i in list:
#         print(i.title())
    

#     choose = int(input('Enter the choose:'))
#     if choose == 1:
#         n = int(input('Enter to append:'))
#         ch.add(n)
#         print('List:', ch.display())
    

#     elif choose == 2:
#         n = int(input('Enter to remove:'))
#         ch.remove(n)
#         print('List:', ch.display())
    
#     elif choose == 3:
#         print('List:', ch.display())
    
#     elif choose == 0:
#         print('Exiting.')
    
#     else :
#         print('Invalid choice.')
    

# print()

'''Sample calulator'''
 
# class Calculator():
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
    
#     def addition(self):
#         return self.a + self.b 
    
#     def subtraction(self):
#         return self.a - self.b 
    
#     def multiplication(self):
#         return self.a * self.b 
    
#     def division(self):
#         if self.b == 0:
#             print('opps wrong input')
#         else:
#             return self.a / self.b
        


# a = int(input('Enter the first num:'))
# b = int(input('Enter the second num:'))

# cal = Calculator(a, b)

# choice = 1

# while choice != 0:
#     list = ['0. exit', '1. addition', '2. subtraction', '3. multiplication', '4. division']
#     for i in list:
#         print(i.title())
    
#     choice  = int(input('Enter your choice:'))
#     if choice == 1:
#         print('Resul:', cal.addition())
    
#     elif choice == 2:
#         print('Resul:', cal.subtraction())
#     elif choice == 3:
#         print('Result:', cal.multiplication())
    
#     elif choice == 4:
#         print('Result:', cal.division())
#     elif choice == 0:
#         print("Exiting!")
#     else:
#         print('Invalid input!')
    
# print()


