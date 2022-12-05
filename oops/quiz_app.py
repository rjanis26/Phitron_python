 
import random

''' intro the game''' 
def display_intro():
    title = '** Simple Math Quiz**'
    print('*'* len(title))
    print(title)
    print('*' * len(title))


''' Menu list'''
def menu_list():
    menu_bar = ['1. addition', '2. subtraction', '3 multiplication', 'Integer division', 'exit']
    for x in menu_bar:
        print(x.title()) 

'''separtor'''
def separtor():
    print('-' * 25)


'''input from user'''
def get_user_input():
    user_input = int(input('Enter the choice:>>> '))
    while user_input > 5 or user_input <= 0:
        print('Invalid menu input!')
        user_input = int(input('Please try agian:>>> '))
    else:
        return user_input
    

''' get user solutions'''
def get_user_solution(problem):
    print('Enter your answer:>>> ')
    print(problem, end='') 
    result = int(input(' = '))
    return result 


'''check solution'''
def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count += 1 
        print('Correct.')
        return count 
    else:
        print('Incorrect.')
        return count 


def menu_option(choice, count):
    num1 = random.randrange(1, 51)
    num2 = random.randrange(1, 51)

    if choice is 1:
        problem = str(num1) + ' + ' + str(num2)
        solution = num1 + num2 
        user_solution = get_user_solution(problem) 
        count = check_solution(user_solution, solution, count)
        return count 
    
    
    elif choice is 2:
        problem = str(num1) + '-+ ' + str(num2)
        solution = num1-+ num2 
        user_solution = get_user_solution(problem) 
        count = check_solution(user_solution, solution, count)
        return count

    elif choice is 3:
        problem = str(num1) + '*+ ' + str(num2)
        solution = num1 * num2 
        user_solution = get_user_solution(problem) 
        count = check_solution(user_solution, solution, count)
        return count

    else:
        problem = str(num1) + '// ' + str(num2)
        solution = num1 // num2 
        user_solution = get_user_solution(problem) 
        count = check_solution(user_solution, solution, count)
        return count


def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100),2)
    
    if total == 0:
        percentage = 0
        
    print("You answerd", total, "questions with", correct, " correct.")
    print("Your score is ", percentage, "%. Thank you.", sep="")


def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100),2)
    
    if total == 0:
        percentage = 0
        
    print("You answerd", total, "questions with", correct, " correct.")
    print("Your score is ", percentage, "%. Thank you.", sep="")
                 
    
    
    
def main():
    display_intro()
    menu_list()
    separtor()
    get_user_input()
 
    option = get_user_input()
    total = 0
    correct = 0
    
    while option != 5:
        total += 1
        correct = menu_option(option, correct)
        option = get_user_input()
    
    print("Exit The Quiz.")
    separtor()
    display_result(total, correct)
    
    
main()
                 

""" 
import random

def display_intro():
    title = "** A Simple Math Quiz **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))
    
def display_menu():
    menu_list = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Integer Division", "5. Exit"]
    for menu in menu_list:
        print(menu)
    
def display_separator():
    print("-" * 24)
    
def get_user_input():
    user_input = int(input("Enter your choice:"))
    while user_input > 5 or user_input <= 0:
        print("Invalid menu option!.")
        user_input = int(input("Please try again:"))
    else:
        return user_input
    
def get_user_solution(problem):
    print("Enter your answer:")
    print(problem, end="")
    result = int(input(" = "))
    return result

def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count += 1
        print("Correct.")
        return count
    else:
        print("Incorrect.")
        return count

def menu_option(index, count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    
    if index == 1:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution,count)
        return count
    elif index == 2:
        problem = str(number_one) + " - " + str(number_two)
        solution = number_one - number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    
    elif index == 3:
        problem = str(number_one) + " * " + str(number_two)
        solution = number_one * number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution,count)
        return count
    
    else:
        problem = str(number_one) + " // " + str(number_two)
        solution = number_one // number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution,count)
        return count
    
def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100),2)
    
    if total == 0:
        percentage = 0
        
    print("You answerd", total, "questions with", correct, " correct.")
    print("Your score is ", percentage, "%. Thank you.", sep="")
                 
    
    
    
def main():
    display_intro()
    display_menu()
    display_separator()
    get_user_input()
 
    option = get_user_input()
    total = 0
    correct = 0
    
    while option != 5:
        total += 1
        correct = menu_option(option, correct)
        option = get_user_input()
    
    print("Exit The Quiz.")
    display_separator()
    display_result(total, correct)
    
    
main() """


