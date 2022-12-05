  
# class Check():
#     def __init__(self):
#         self.n = [] 
    
#     def add(self, a):
#         return self.n.append(a)
    
#     def remove(self, b):
#         self.n.remove(b)
    
#     def display(self):
#         return (self.n) 
    

# ch = Check()
# choice = 1 

# while choice != 0:
#     menu_list = ['0. exit', '1. add', '2. delete', '3. dispaly']
#     for x in menu_list:
#         print(x.title()) 

    
#     choice = int(input('Enter choice>>> '))
#     if choice == 1: 
#         data = int(input('Enter data to append>>> '))
#         ch.add(data)
#         print('List: ', ch.display())
    
#     elif choice == 2:
#         data = int(input('Enter data to remove>>> '))
#         ch.remove(data)
#         print('List: ', ch.display()) 

#     elif choice == 3:
#         print('List: ', ch.display()) 
    
#     elif choice == 0:
#         print('Exiting!')
    
#     else:
#         print('Invalid choice!!')

# print()


''' check valid parenthesis'''
  
class Solution:
    def is_valid(self, str):
        stack, pchar = [], {'(' : ')', '{':'}', '[':']'}
        for parenthese in str:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False 
        return len(stack) == 0


s = Solution()
print(s.is_valid('(){}[]'))
print(s.is_valid('()[{)}'))
print(s.is_valid('(){}'))
