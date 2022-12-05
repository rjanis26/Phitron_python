
# =======================================
# First Lab Exam 
# ========================================
#Question: 01

# def  create_string(string_List):
#     return ' '.join([x for x in string_List])

# print(create_string(['This', 'is', 'Using', 'List']))

# def create_string(List):
#     return ' '.join(map(str, List))

# print(create_string(['this', 'is', 'noraml', 'for', 'Sure']))
# print(create_string(['Hello', 'world', 'hourseful']))

#Question: 01
 

# #Question: 07

# def replace_comma_with_space(str):
#     return str.replace(',', ' ')


# str = input('Enter the string:')
# print(replace_comma_with_space(str))
 

# Question:08 

# def test_script(str):
#     def make_upper():
#         return str.upper()
#     print(make_upper())
#     def make_caplital():
#         return str.capitalize()
#     print(make_caplital())

#     def make_lower():
#         return str.lower()
#     print(make_lower())

# str = input("Enter the string:")
# test_script(str)
 

# def test_script(str):
#     def make_upper():
#         print(str.upper())
#     make_upper()  #call the function...

#     def make_capital():
#         print(str.capitalize())
#     make_capital()
     
#     def make_lower():
#         print(str.lower())
#     make_lower()
        

# str = input("Enter the string:")
# test_script(str)


# Question:05


# x = {'a':1, 'b': 2, 'c': 3, 'd': 4}
# # print(list(x.items()))

 
# #for string operations
# import string	
# s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"

# clean_tweet=[]
# #remove punctuations
# for word in s:
# 	if word not in string.punctuation:
# 		clean_tweet.append(word)
#         print(''.join([x for x in clean_tweet]))

# print("clean_tweet = {}".format(clean_tweet))


# Question: 06

# import string
# def clean_string(str):
#     clean_str =[]
#     for word in str:
#         if word not in string.punctuation:
#             clean_str.append(word)
#     return ''.join([x for x in clean_str])


# str = input("Enter the string:")
# print(clean_string(str))

# def print_hi():
#     print('hi')
#     # return ("hi")

# # print(print_hi()) 
# print_hi()


# from bs4 import BeautifulSoup
# import requests
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 
 
# def weather_data(city):
#     city = city.replace(" ", "+")
#     res = requests.get(
#         f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
#     print("Searching...\n")
#     soup = BeautifulSoup(res.text, 'html.parser')
#     location = soup.select('#wob_loc')[0].getText().strip()
#     time = soup.select('#wob_dts')[0].getText().strip()
#     info = soup.select('#wob_dc')[0].getText().strip()
#     weather = soup.select('#wob_tm')[0].getText().strip()
#     print(location)
#     print(time)
#     print(info)
#     print(weather+"°C")
 
 
# city = input("Enter the Name of City ->  ")
# city = city+" weather"
# weather_data(city)
  
def replace_word(replace_with, s):
    str1 = s.split()
    for i, word in enumerate(replace_with):
        if not i&1:
            for j, word2 in enumerate(str1):
                if word == word2:
                    str1[j] = replace_with[i+1]
    return ' '.join(str(x) for x in str1)

 

# replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

# s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

# print(replace_word(replace_with, s))



# def clean_string(text):
#     str = ""
#     for s in text:
#         if s.isalpha():
#             str += s
#     return ' '.join(x for x in str)

# print(clean_string("P::::::,,,,,h;;;;i,,,t--r;,:o..N"
# ))

# def solve(D):
#     res = []
#     for k, v in D.items():
#         res.extend([k,v])
#     return res

# print(solve({ 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}))