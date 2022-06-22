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

prompt = "Enter your age "
prompt += "(Enter 'quit' to end the program)"
age = ""
while age != 'quit':
    if age != 'quit':
        age = input(prompt)
        age = int(age)
        if age < 3:
            print("Ticket is free")
        elif age < 12:
            print("ticket is $10")
        elif age > 12:
            print("ticket is $15")
    else:
        break

# using while loop with lists and dictionaries
# moving items between lists
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Veifying user:{current_user.title()}")
    confirmed_users.append(current_user)
print("The following users are verified: ")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# removing all instances of value from a list
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# filling a dictionnary with a user input
responses = {}
polling_active = True
while polling_active:
    name = input(f"\nWhat is your name? ")
    response = input("Which mountain would you lik to climb? ")
    responses[name] = response
    repeat = input('Would you like another person to response? (yes/no)')
    if repeat == 'no':
        polling_active = False
print(f"\n---Polling Results---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}")

# ex 7-8
sandwich_orders = ['tuna', 'egg', 'chicken', 'salad', 'prawns']
finished_sandwiches = []
while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()
    print(f"Preparing: {preparing_sandwich} sandwich")
    finished_sandwiches.append(preparing_sandwich)
for finished_sandwich in finished_sandwiches:
    print(f"Ready to serve: {finished_sandwich} sandwich")

sandwich_orders = ['tuna', 'pastrami', 'pastrami',
                   'egg', 'chicken', 'pastrami', 'salad', 'prawns']
print(sandwich_orders)
print('Deli has run out of pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

dream_vacation = {}
polling_active = True
while polling_active:
    name = input("Name?")
    location = input('location?')
    dream_vacation[name] = location
    repeat = input('Would you like another person to response? (yes/no)')
    if repeat == 'no':
        polling_active = False
for name, location in dream_vacation.items():
    print(f"{name.title()}'s favourite location is {location.title()}")
