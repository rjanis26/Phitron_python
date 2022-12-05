

# https://medium.com/@gurupratap.matharu/object-oriented-programming-project-in-python-for-your-github-portfolio-d34feaf1332c
# class Vehicale():
#     ''' Base class for all vehicals '''
#     def __init__(self, name, color, manufacturer):
#         self.name = name
#         self.color = color 
#         self.manufacturer = manufacturer
    
#     def drive(self):
#         print('Driving......', self.manufacturer, self.name)
    
#     def turn(self, direction):
#         print('Turning', self.name, 'to', direction)
    
#     def brake(self):
#         print(self.name,'is Stoping....')


# class Car(Vehicale):
#     ''' car class '''
#     def __init__(self,name, color, manufacturer, year):
#         self.year = year
#         super().__init__(name, color, manufacturer)

#     def __str__(self):
#         return ('Name:{}\nColor:{}\nManufacturer:{}\nYear:{}'.format(self.name, self.color, self.manufacturer, self.year))
    
#     def change_gear(self, gear_name:str):
#         print('{} is changing gear {}'.format(self.name, gear_name))


# v1 = Vehicale('Fusion 110 EX', 'Whilte', 'Walton')
# # v1.drive()
# # v1.turn('Left')
# # v1.brake()

# car = Car('Lambargini', 'Black', 'Ford Dana', 2012)

# print(car)
# car.change_gear('R')

# print('******** car_2 Info **********')
# car2 = Car('Ferai Xd202', 'Red', 'Ferari Dana', 2022)
# print(car2)
# car2.change_gear('P')


# class Person():
#     def __init__(self, name:str, age:int, height:float):
#         self.name = name
#         self.age = age
#         self.height = height
    

# class Student(Person):
#     def __init__(self, name, age, height, roll, gpa, section):
#         super().__init__(name, age, height)
#         self.roll = roll
#         self.gpa = gpa
#         self.section = section

#     def __str__(self):
#         return f'Name:{self.name}\nAge:{self.age}\nHeight:{self.height}\nRoll:{self.roll}\nGPA:{self.gpa}\nSection:{self.section}'

#     def is_adult(self, age):
#         print('Congratultions. You can vote') if self.age >= age else print('Opps! You can not vote')

#     def is_capable(self, limit):
#         if self.age > limit:
#             print(self.name, 'is not capable.')
#         else:
#             print(self.name,'is capable.')
    


# person = Person('Anisul islam', 20,5.6)
# # print(person.age)
# # print(person.name)

# student = Student('Akram khan', 21, 5.6, 3432, 4.33, 'A')
# print(student)
# student.is_adult(14)
# student.is_capable(55)


# class Staff:
#     def __init__(self, role, dept, salary):
#         self.role = role 
#         self.dept  = dept
#         self.salary = salary
    
#     def show_details(self):
#         print('Name:{}\nAge:{}\nDepartment:{}\nSalary:{}'.format(self.role, self.dept, self.salary))


# # inherit from the staff class
# class Teacher(Staff):
#     def __init__(self, role, dept, salary, name, age):
#         super().__init__(role, dept, salary)
#         self.name = name
#         self.age = age
        

# teacher = Teacher('Teaching', 'English', 2435, 'Anisul', 24)
# res = (teacher.__dict__)
# for k,v in res.items():
#     print(k, v)

 

# class Staff():
#     def __init__(self, role, dept, salary):
#         self. role = role
#         self.dept = dept
#         self.salary = salary
    
#     def show_details(self):
#         print('Name:{}\nAge:{}\nDepartment:{}\nSalary:{}'.format(self.role, self.dept, self.salary))


# class Tearcher(Staff):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__('Tearcher', 'English', 35530)
    

# teacher = Tearcher('Rakibul islam', 45)
# teacher.show_details()


''' Implement the stack '''

# class Stack():
#     def __init__(self):
#         self.__stack = []
    
#     def push(self, item):
#         self.__stack.append(item)
    
#     def pop(self):
#         self.__stack.pop()
    
#     def traverse(self):
#         for item in self.__stack[::-1]:
#             print(item, end=' ')


# st = Stack()

# for i in range(1, 11):
#     st.push(i)


# st.traverse()
# st.pop()
# st.pop()
# print('\n')

# st.traverse()


# class Person():
#     def __init__(self, name, id:int):
#         self.name = name
#         self.id = id 
    
#     def display(self):
#         print('Naem:{}\nId:{}'.format(self.name, self.id))
    
#     def details(self):
#         print('My name is {} and Id is {}'.format(self.name, self.id))
    

# class Employee(Person):
#     def __init__(self, name, id: int, salary, post):
#         super().__init__(name, id)
#         self.salary = salary
#         self.post = post
    
#     def show(self):
#         print('My name is {}, Id {} and Post {}'.format(self.name, self.id, self.post))
    


# emp = Employee('Hamidur Rahman', 12423, 50000, 'Intern')
# emp.details()
# emp.show()


# class Employee:
#     def __init__(self, name, age, salary):
#         self.name = name 
#         self.age = age
#         self.salary = salary

# class SoftwareEngineer(Employee):
#     def __init__(self, name, age, salary, level):
#         super().__init__(name, age, salary)
#         self.level = level

#     def print_details(self):
#         print('Name:{}\nAge:{}\nSalary:{}\nLevel:{}'.format(self.name, self.age, self.salary, self.level))
    


# class Designeer(Employee):
#     def work(self):
#         print(f'{self.name} is designing...')
    
#     def draw(self):
#         print(f'{self.name} is drawing.....')
    

# se = SoftwareEngineer('Anisul islam', 21, 45600, 'Junior')
# se.print_details()
# de = Designeer('Halim', 40, 5000)
         
# de.work() 
# de.draw() 

 

# class Employee():
#     def __init__(self, name, salary = 0):
#         self.name = name 
#         self.salary = salary

#     def give_raise(self, percent):
#         self.salary += self.salary *percent
    
#     def work(self):
#         print(self.name, 'does stuff')
    
#     def __repr__(self):
#         return 'Name:{} Salary:{}'.format(self.name, self.salary)
    

# class Chef(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
    
#     def work(self):
#         print(self.name, 'makes food')

# class Server(Employee):
#     def __init__(self, name, salary=0):
#         super().__init__(name, salary)

#     def work(self):
#         print(self.name, 'interfaces with coustomer.')

# class PizzaRobot(Chef):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
    
#     def work(self):
#         print(self.name, 'makes pizza')


# if __name__ == '__main__':
#     bob = PizzaRobot('Bulbul', 2500)
#     ser = Server('Rajom khan', 4000)
#     ch = Chef('Food bozz', 6000)
#     print(bob)
#     bob.work()
#     bob.give_raise(0.20)
#     print(bob); print()

#     for klass in Employee, Server, PizzaRobot, Chef:
#         res = klass(klass.__name__)
#         res.work()



# class Employee:
#  def __init__(self, name, salary=0):
        
#     self.name = name
#     self.salary = salary
#  def giveRaise(self, percent):
#     self.salary = self.salary + (self.salary * percent)
#  def work(self):
#     print(self.name, "does stuff")
#  def __repr__(self):
#     return "<Employee: name=%s, salary=%s>" % (self.name, self.salary)
# class Chef(Employee):
# # OOP and Inheritance: “Is-a” Relationships | 935
#     def __init__(self, name):

#      Employee.__init__(self, name, 50000)
#      def work(self):
#          print(self.name, "makes food")

# class Server(Employee):
#     def __init__(self, name):
#         Employee.__init__(self, name, 40000)
#     def work(self):
#         print(self.name, "interfaces with customer")

# class PizzaRobot(Chef):
#     def __init__(self, name):
#         Chef.__init__(self, name)
#     def work(self):
#         print(self.name, "makes pizza")

# if __name__ == "__main__":
#  bob = PizzaRobot('bob') # Make a robot named bob
#  print(bob) # Run inherited __repr__
#  bob.work() # Run type-specific action
#  bob.giveRaise(0.20) # Give bob a 20% raise
#  print(bob); print()
#  for klass in Employee, Chef, Server, PizzaRobot:
#     obj = klass(klass.__name__)
#     obj.work()

# class Solution():
#     def __init__(self, x, y):
#         self.x = x 
#         self.__y = y 
    
#     def details(self):
#         print('X:', self.x, 'Y:', self.__y)


# s = Solution(5, 10)
# s.details()

 

# class Student():
#     def __init__(self, name, id):
#         self.name = name 
#         self.__id = id 
    

#     @property
#     def details(self):
#         print('Name:{} Id:{}'.format(self.name, self.__id))
#         self.__methods()

#     def __methods(self):
#         print('This is private mathod Excuted')
    


# s = Student('anisul islam', 13)
# s2 = Student('Rakbil islam', 32)

# s.details
# s2.details
# # s.__methods()

''' Static Variable'''

# class Player():
#     total_score = 0

#     def __init__(self, run):
#         self.run = run 
    
#     def hit_four(self):
#         self.run += 4 
#         Player.total_score += 4 
    
#     def hit_six(self):
#         self.run += 6 
#         Player.total_score += 6


# if __name__ == '__main__':
#     print(Player.total_score)
#     sakib = Player(0)
#     tamim = Player(0) 

#     tamim.hit_four()
#     sakib.hit_six()
#     tamim.hit_four()
#     sakib.hit_six()

#     print('Sakib:', sakib.run)
#     print('tamim:', tamim.run)

#     print(Player.total_score)

 

# class Student():
#     student_count = 0
#     def __init__(self, name, id):
#         self.name = name 
#         self.id = id 
#         Student.student_count += 1
    

#     def details(self):
#         print('Name:{} Id:{}'.format(self.name, self.id))
 

# if __name__ == '__main__':
#     print(Student.student_count)

#     s1 = Student('Anisul', 43)
#     s2 = Student('Akram', 50)
#     s3 = Student('Rakibul', 101)
#     s4 = Student('Roni', 4050)

    # print('Total student:',Student.student_count)
     
''' class Method'''
  

# class Student:
#     uni_name = 'BracU'

#     def __init__(self, name, id):
#         self.name = name 
#         self.__id = id 
    
#     def details(self):
#         print('Name:{}, Id:{}, Uni:{}'.format(self.name, self.__id, Student.uni_name))


#     @classmethod
#     def updat_uni_name(cls, new_name):
#         cls.uni_name = new_name


#     @classmethod
#     def from_string(cls, info):
#         name, id = info.split('-')
#         return cls(name, id)


# # s = Student('Roni', 50) 
# # s.details()
# # Student.updat_uni_name('Brac University')
# # s.details()


# # s2 = Student('monirul islam', 532)
# # s2.details()
# s = Student('Anis', 50)
# s2 = Student.from_string('Carol-560')
# s2.details()

''' Static method'''

# class Student:
#     uni_name = 'BracU'

#     def __init__(self, name, id):
#         self.name = name 
#         self.__id =  id 

    
#     def details(self):
#         print('Name: {} Id:{} Uni_name: {}'.format(self.name, self.__id, Student.uni_name)) 
    
#     @classmethod
#     def update_uni_name(cls, newName):
#          cls.uni_name = newName;
    
#     @staticmethod
#     def check_dept(id):
#         if id[3:5] == '01' : print('CSE')
#         elif id[3:5] == '47': print('CS')
#         elif id[3:5] == '56': print('BBA')
    


# if __name__ == '__main__':
#     st = Student('anisul islam', 45)
#     st.details()
#     st2 = Student('Rakibul islam', 563)
#     st.details() 
#     Student.update_uni_name('Brac University.')
#     st.details()
#     st2.details()
#     Student.check_dept('235010945')
#     Student.check_dept('13447623')
#     Student.check_dept('1315678')

  
# class Engine():
#     def __init__(self, cc):
#         self.capacity = cc 
    
#     def start(self):
#         print('Engine started.')
    
#     def stop(self):
#         print('Engine stopped.')

# class Car(Engine):
#     def __init__(self,name, cc):
#         self.name = name 
#         super().__init__(cc)
    
#     def run(self):
#         self.start()
#         print('Car is runnig.') 

 
# if  __name__ == '__main__':
#     car = Car('BMW', 4500)
#     car.run()


''' class method and static method'''
  
# class Student:
#     school_name = 'ABC School'
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age 
    

#     def show(self):
#         return 'Name:{} Age: {} School_name: {}'.format(self.name, self.age, Student.school_name) 
    
#     @classmethod
#     def change_school(cls, name):
#         cls.change_school = name 


# https://github.com/ugurcanerdogan/cinema-hall-project/blob/main/Main.py
#https://github.com/ugurcanerdogan/cinema-hall-project 

 