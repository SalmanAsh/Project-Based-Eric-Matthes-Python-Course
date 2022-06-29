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
