#Files and Exceptions

# reading an entire file

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
