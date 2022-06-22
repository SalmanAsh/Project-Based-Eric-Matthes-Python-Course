# User input and while loops
# input()
message = input('tell me something, i will repeat it.')
print(message)

# writing clear prompt
name = input('Please enter your name:')
print(f"Hello, {name.title()}")

prompt = "tell me about yourself, "
prompt += "what is your name?"
name = input(prompt)
print(f"\tHello, {name.title()}")

# using int()
age = input("How old are you?")
print(age)
int(age) >= 18

age = input("How old are you?")
print(age)
age = int(age)
age

height = input("How tall are you?")
height = int(height)
if height >= 1.70:
    print(f"\nYou are tall enough")
else:
    print(f"\nYou are too short")

# modulo operator
4 % 3
5 % 3
6 % 3
7 % 2

number = input("Enter a number")
number = int(number)
if number % 2 == 0:
    print(f"The number {number} is even")
else:
    print(f"The number {number} is odd ")

# While loops
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number = current_number + 1

current_number = 1
while current_number >= -5:
    print(current_number)
    current_number -= 1

# letting the user choose when to quit
prompt = "\nTell me something"
prompt += "Enter quit to end the program"
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

prompt = "\nTell me something"
prompt += "Enter quit to end the program"
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)

# using a flag
prompt = "\nTell me something"
prompt += "Enter quit to end the program"
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# using break to exit the loop
prompt = "Enter the name of the city you visited "
prompt += "(Enter 'quit' to end the program)"
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I would love to go to {city.title()}")

# using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1

# ex 7-4
prompt = "Enter the toppings you want "
prompt += "(Enter 'quit' to end the program)"
toppings = ""
while toppings != 'quit':
    toppings = input(prompt)
    if toppings != 'quit':
        print(f"{toppings} added")
