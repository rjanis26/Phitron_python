# class Student():
#     def __init__(self, id:int, name:str, class_name:str):
#         self. id = id 
#         self.name = name
#         self.class_name = class_name



# student = Student(10012, 'Frank Gibson', 'Bigo')

# for k, v in student.__dict__.items():
#     print(k, v)


# https://www.techgeekbuzz.com/blog/python-object-oriented-programming-exercise/#:~:text=Python%20OOPs%20Exercise%201%3A%20Write%20a%20Program%20to,creation%2C%20we%20can%20define%20the%20__init__%20%28%29%20method.

 

# class Car():
#     def __init__(self, name:str, color:str):
#         self.name = name
#         self.color = color
    
#     def start(self):
#         print('Name:{}\nColor:{}'.format(self.name, self.color))



# car = Car('Honda', 'Blue')
# car.start()
  
# class Car():
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color 
#     def start(self):
#         print('Starting the engine.')


# car= Car('Lambargini', 'White')
 
# print(car.name, car.color, car.year)

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




# import math 
# n = int(input('>>> '))

# def is_prime(n):
#     for i in range(2, int(math.sqrt(n)+1)):
#         if n % i == 0:
#             return False 
#     return True 



# for i in range(2, n+1):
#     if is_prime(i):
#         print(i, end=' ')








# ======================================================================================================
#                                     Zulkarnine tutorial
# =====================================================================================================

""" 
class Person:
    def __init__(self, name, dateofBirth:int, height:float):
        self.name = name 
        self.dateofBirth = dateofBirth
        self.height = height 
 
    def get_name(self):
        return self.name


    def set_name(self,new_name):
        if self.__has_num(new_name):
            print('Sorry person name can not num.')
            return 
        self.name = new_name 

    
    def __has_num(self, string):
        return "0" in string 

    
    def get_summary(self):
        return 'Name:{} DateOfBirth:{} Height: {}'.format(self.name, self.dateofBirth, self.height)
     


p = Person('anisul islam', 1990, 6.5)
print(p.get_summary())
print(p.get_name())
p.set_name = 'Hello world'
print(p.get_name())
print(p.get_summary())

  """

""" 
class Bank:
    def __init__(self):
        self.client_details_list = []
        self.loggedin = False
        self.cash = 100
        self.TranferCash = False

    def register(self, name , ph , password):
        cash = self.cash
        contitions = True
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number ! please enter 10 digit number")
            contitions = False

        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
            contitions = False  
        
        if contitions == True:
            print("Account created successfully")
            self.client_details_list = [name , ph , password , cash]
            with open(f"{name}.txt","w") as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")


    def login(self, name , ph , password):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in str(self.client_details_list):
                if str(password) in str(self.client_details_list):
                    self.loggedin = True

            if self.loggedin == True:
                print(f"{name} logged in")
                self.cash = int(self.client_details_list[3])
                self.name = name
            
            else:
                print("Wrong details")

    def add_cash(self, amount):
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
            
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(self.cash)))

            print("Amount added successfully")

        else:
            print("Enter correct value of amount")

    def Tranfer_cash(self, amount , name ,ph):
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in self.client_details_list:
                self.TranferCash = True

        
        if self.TranferCash == True:
            total_cash = int(self.client_details_list[3]) + amount
            left_cash = self.cash - amount
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(total_cash)))

            with open(f"{self.name}.txt","r") as f:
                details_2 = f.read()
                self.client_details_list = details.split("\n")
            
            with open(f"{self.name}.txt","w") as f:
                f.write(details_2.replace(str(self.client_details_list[3]),str(left_cash)))

            print("Amount Transfered Successfully to",name,"-",ph)
            print("Balacne left =",left_cash)

    def password_change(self, password):
        if len(password) < 5 or len(password) > 18:
            print("Enter password greater than 5 and less than 18 character")
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[2]),str(password)))
            print("new Password set up successfully")
        
    def ph_change(self , ph):
        if len(str(ph)) > 10 or len(str(ph)) < 10:
            print("Invalid Phone number ! please enter 10 digit number")
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[1]),str(ph)))
            print("new Phone number set up successfully")



if __name__ == "__main__":
    Bank_object = Bank()
    print("Welcome to my Bank")
    print("1.Login")
    print("2.Creata a new Account")
    user = int(input("Make decision: "))

    if user == 1:
        print("Logging in")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Bank_object.login(name, ph, password)
        while True:
            if Bank_object.loggedin:
                print("1.Add amount")
                print("2.Check Balcane")
                print("3.Tranfer amount")
                print("4.Edit profile")
                print("5.Logout")
                login_user = int(input())
                if login_user == 1:
                    print("Balance =",Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    Bank_object.add_cash(amount)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                
                elif login_user == 2:
                    print("Balacne =",Bank_object.cash)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break

                elif login_user == 3:
                    print("Balance =",Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    if amount >= 0 and amount <= Bank_object.cash:
                        name = input("Enter person name: ")
                        ph = input("Enter person phone number: ")
                        Bank_object.Tranfer_cash(amount,name,ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif amount < 0 :
                        print("Enter please correct value of amount")

                    elif amount > Bank_object.cash:
                        print("Not enough balance")

                elif login_user == 4:
                    print("1.Password change")
                    print("2.Phone Number change")
                    edit_profile = int(input())
                    if edit_profile == 1:
                        new_passwrod = input("Enter new Password: ")
                        Bank_object.password_change(new_passwrod)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 2:
                        new_ph = int(input("Enter new Phone Number: "))
                        Bank_object.ph_change(new_ph)
                        print("\n1.back menu")
                        print("2.Logout")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break

                elif login_user == 5:
                    break
                        
                    
    if user == 2:
        print("Creating a new  Account")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        password = input("Enter password: ")
        Bank_object.register(name, ph, password) """
 



# class Device:
#     def __init__(self, brand, color, price):
#         self.brand = brand 
#         self.color = color 
#         self.price = price 
 

# class Laptop(Device):
#     def __init__(self, brand, color, price, ram, rom):
#         super().__init__(brand, color, price)
#         self.ram = ram 
#         self.rom = rom 
    
#     def __str__(self):
#         return 'Brand:{} Color:{} Price:{}tk Ram:{}GB Rom:{}GB'.format(self.brand, self.color, self.price, self.ram, self.rom)


# class Phone(Laptop):
#     def __init__(self, brand, color, price, ram, rom, year):
#         super().__init__(brand, color, price, ram, rom)
#         self.year = year 
     
#     def __repr__(self):
#         return 'Brand:{} Color:{} Price:{}tk Ram:{}GB Rom:{}GB Year:{}'.format(self.brand, self.color, self.price, self.ram, self.rom, self.year)

 

# if __name__ == '__main__':
#     l = Laptop('HP', 'Silver', 50000, 8, 256)
#     print(l)
#     phone = Phone('Apple', 'Black', 900000, 8, 256, 1989)
#     print(phone)
#     print(phone.__dict__)

 
 

# class Person:
#     def __init__(self, name:str, year_of_birth:int, height_inc:int = None):
#         self.__name = name 
#         self.__year_of_birth = year_of_birth 
#         self.__height = height_inc 

#     def get_summary(self):
#         return f'Name:{self.__name} DOB:{self.__year_of_birth} Height:{self.__height if self.__height is not None else "Invalid"}'

#     def set_name(self, newName):
#         if(self.__has_any_num(newName)):
#             print('Name can not have numbers.')
#             return 
#         else:
#              self.__name = newName 
    
#     def get_name(self):
#         return self.__name 

#     def get_date_of_birth(self):
#         return self.__year_of_birth

#     def __has_any_num(self, string):
#         return "0" in string

# # p = Person('Anisul islam', 2001, 65) 
# # print(p.get_summary()) 
# # p.set_name("9akmal islma")
# # print(p.get_name())
# # print(p.name)

# person_list = [Person('anisul', 1990, 65), Person('bokilla', 2002, 56), Person('Ratul', 1965), Person('salman', 1985, 50), Person('rafiq', 20003)] 
 
# for person in person_list:
#     if person.get_date_of_birth() >= 1960:
#         print(person.get_summary())

