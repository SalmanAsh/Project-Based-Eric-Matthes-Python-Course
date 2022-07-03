# Files and Exceptions

# reading an entire file

import json
with open('pi_digits.txt') as file_object:
    content = file_object.read()
    print(content)

with open('pi_digits.txt') as file_object:
    content = file_object.read()
    print(content.rstrip())

# file path
with open('text_files/pi_digits.txt') as file_object:
    content = file_object.read()
    print(content)

# reading line by line

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line)

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

# making a list of line from a file
with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# working with files content
file_content = 'pi_digits.txt'
with open(file_content) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))


file_content = 'pi_digits.txt'
with open(file_content) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# large files
with open('Resources/pi_million_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:50])
print(len(pi_string))

# is your birthday in pi
with open('Resources/pi_million_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()

"""
birthday=input("Entre your birthday in form ddmmyy")
if birthday in pi_string:
    print('yes')
else:
    print('no')
"""
# ex 10-1
message = 'I like pizza'
message.replace('pasta', 'pizza')
print(message)

# writing to an empty file
file_name = 'Resources\programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write('I love programming')

file_name = 'Resources\programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write('I love programming too')

# writting multiple lines
file_name = 'Resources\programming.txt'
with open(file_name, 'w') as file_object:
    file_object.write('I love programming too. \n')
    file_object.write('I love python \n')

# appending to a file
file_name = 'Resources\programming.txt'
with open(file_name, 'a') as file_object:
    file_object.write('I like maths too, ')
    file_object.write('and physics too')

# Exceptions
# ZeroDivisionError exception
"""print(5/0)"""

# try-except block
try:
    print(5/0)
except ZeroDivisionError:
    print("You cannot divide by zero")

# using exceptions to prevent crashes

print('Give me two numbers, I will divide them')
print('Enter q to exit')
while True:
    first_number = input('\n first number')
    if first_number == 'q':
        break
    second_number = input('second number')
    if second_number == 'q':
        break
    answer = int(first_number)/int(second_number)
    print(answer)

print('Give me two numbers, I will divide them')
print('Enter q to exit')
while True:
    first_number = input('\n first number')
    if first_number == 'q':
        break
    second_number = input('second number')
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
        print(answer)
    except ZeroDivisionError:
        print('You cannot divide by zero')

# the else block


print('Give me two numbers, I will divide them')
print('Enter q to exit')
while True:
    first_number = input('\n first number')
    if first_number == 'q':
        break
    second_number = input('second number')
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print('You cannot divide by zero')
    else:
        print(answer)

# FileNotFoundError exception

filename = 'alice.txt'
with open(filename, encoding='utf-8') as f:
    content = f.read()

filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print('file does not exists')

# analysing text
title = "Alice in Wonderland"
title.split()

filename = 'Resources/alice.txt'
try:
    with open(filename, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print('File does not exists')
else:
    """Counting words"""
    words = content.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words")

# working with multiple files


def count_words(filename):
    """Count the approximated number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("File does not exist")
    else:
        words = content.split()
        print(len(words))


count_words('Resources/alice.txt')

filenames = ['Resources/alice.txt', 'Resources/pi_million_digits.txt',
             'Resources/programming.txt', 'Resources/hello.txt']
for filename in filenames:
    count_words(filename)

# failing silently


def count_words(filename):
    """Count the approximated number of words in a file"""
    try:
        with open(filename, encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        pass
    else:
        words = content.split()
        print(len(words))


filenames = ['Resources/alice.txt', 'Resources/pi_million_digits.txt',
             'Resources/programming.txt', 'Resources/hello.txt']
for filename in filenames:
    count_words(filename)

# ex 10-6

print("Addition of two numbers")
print("enter q to exit")

while True:
    first_number = input("First Number")
    if first_number == 'q':
        break
    second_number = input('second number')
    if second_number == 'q':
        break
    try:
        Total = int(first_number)+int(second_number)
    except ValueError:
        print("Please enter a numerical value")
    else:
        print(Total)


filename = 'Resources/dog.txt'
try:
    with open(filename, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
else:
    print(content)

filename = 'Resources/dog.txt'
try:
    with open(filename, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    pass
else:
    print(content)


file_name = "Resources/alice.txt"
file_name.lower().count('a')

# storing data
# json.dump() and json.load()
numbers = [2, 3, 5, 7, 11, 13]
filename = 'Resources\storing.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

filename = 'Resources\storing.json'
with open(filename) as f:
    numbers = json.load(f)
print(numbers)

# saving and using user data

username = input("Usernane?")
filename = 'Resources/userdata.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"{username} has been stored")

filename = 'Resources/userdata.json'
with open(filename) as f:
    username = json.load(f)
    print(username)

""" load previously stored username"""
"""otherwise, store a new one"""
filename = 'Resources/username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("Enter Username")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print("Username is now saved")
else:
    print(username)

# refactoring


def greet_user():
    filename = 'Resources/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("username")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print("Username is now saved")
    else:
        print(username)


greet_user()


def get_stored_username():
    """Get stored username if available"""
    filename = 'Resources/username.json'
    try:
        with open(filename) as f:
            Username = json.load(f)
    except FileExistsError:
        return None
    else:
        return Username


def greet_user():
    """Greet the user"""
    Username = get_stored_username()
    if Username:
        print(f"Welcome back, {Username}")
    else:
        Username = input("Username")
        with open(filename, 'w') as f:
            json.dump(Username, f)
            print("Username is now saved")


greet_user()


def get_stored_username():
    """Get stored username if available"""
    filename = 'Resources/username.json'
    try:
        with open(filename) as f:
            Username = json.load(f)
    except FileExistsError:
        return None
    else:
        return Username


def get_new_username():
    """Promp for a new username"""
    Username = input("Username")
    with open(filename, 'w') as f:
        json.dump(Username, f)


def greet_user():
    """Greet the user"""
    Username = get_stored_username()
    if Username:
        print(f"Welcome back, {Username}")
    else:
        get_new_username()
        print("Username is now saved")


greet_user()
