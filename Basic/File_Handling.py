 

# try:
#     with open('test1.txt') as f:
#         content = f.read()
#         print(content)
# except Exception as e:
#     print('File handling error:', e)


# try:
#     with open('test.txt') as f:
#         print(f.readlines())
#         # for num, line in enumerate(f):
#         #     print(num+1, line.title())
# except Exception as e:
#     print('File handling error:', e)
   


# try:
#     with open('test.txt', 'r+') as f:
#         print(f.read())
#         f.close()

# except Exception as e:
#     print('File handling Error:', e)

''' find the file size'''

# try:
#     with open('test.txt', 'r+') as f:
#         text = f.read()
#         print(text)
#         print('sizof file:', len(text))
#         f.close()
# except Exception as e:
#     print('File handling error:', e)


# try:
#     with open('test.txt', 'a') as f:
#         f.write('\nSadi - Lecturer of phisics.')
#         f.write('\nBeautifull shoap is a python Library.')
#         f.close()

# except Exception as e:
#     print('File Error:', e)

 


# def file_read(file_name):
#     try:
#         with open(file_name) as f:
#             return f.read()
#     except Exception as e:
#         print('File Error:', e)


# print(file_read('test.txt'))


# def file_read(file_name, n_lines):
#     from itertools import islice
#     try:
#         with open(file_name) as f:
#             for line in islice(f, n_lines):
#                 return line
#     except Exception as e:
#         print('File Error:', e)


# print(file_read('test.txt', 3))


# def file_read_from_head(fname, nlines):
#         from itertools import islice
#         with open(fname) as f:
#                 for line in islice(f, nlines):
#                         print(line)

# file_read_from_head('test.txt',2)

# def read_file(file_name):
#     try:
#         with open(file_name) as f:
#             return f.readlines()
#     except Exception as e:
#         print('File error:', e)


# print(read_file('test.txt'))

 

# def read_file(file_name):

#     try:
#         with open(file_name, 'r') as f:
#             print(f.readlines())
#     except Exception as e:
#         print('File Error:', e)

# read_file('test.txt')

 
# def read_file(file_name):
#     try:
#         res = []
#         with open(file_name) as f:
#             for line in f:
#                 res.append(line)
#             return res
#     except Exception as e:
#         print('File Error:', e)
    
# # print(read_file('test.txt'))
# for ele in read_file('test.txt'):
#     print(ele)


# def longest_word(file_name):
#     try:
#         with open(file_name, 'r') as f:
#             words = f.read().split()
#         max_len = len(max(words, key = len))
#         return [word for word in words if len(word) == max_len]

#     except Exception as e:
#         print('File Error:', e)
    

# print(longest_word('test.txt'))



# def longest_word(file_name):

#     with open(file_name, 'r') as f:
#         words = f.read().split()
#     max_len = len(max(words, key = len))
#     return [word for word in words if len(word) == max_len]
 

# print(longest_word('test.txt'))


# def longest_word(filename):
#     with open(filename, 'r') as infile:
#               words = infile.read().split()
#     max_len = len(max(words, key=len))
#     return [word for word in words if len(word) == max_len]

# print(longest_word('test.txt'))



# replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]

# s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
# str1 = s.split()

# for i, word in enumerate(replace_with):
#     if i % 2 == 0:
#         for j, word2 in enumerate(str1):
#             if word == word2:
#                 str1[j] = replace_with[i+1]

# s = ' '.join(str(x) for x in str1)
# print(s)



# def solve(List):
#     return ' '.join([x for x in List])

# print(solve(["This", "is", "very", "fantastic"]))
