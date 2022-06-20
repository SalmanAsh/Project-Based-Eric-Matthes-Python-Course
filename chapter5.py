# IF statements
cars = ['yahama', 'audi', 'jaguar', 'bmw']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# checking for equality
car = 'bmw'
car == 'bmw'

car = 'Audi'
car.lower() == 'audi'

# checking for inequality
power = 'zero'
if power != 'zero':
    print('hello')
else:
    print('hi')

power = 'zero'
if power != 'z':
    print('hello')
else:
    print('hi')

# numerical comparison
age = 20
age == 20

answer = 17
if answer != 17:
    print('wrong')
else:
    print('right')

age = 20
age > 10

age = 20
age < 5

age = 20
age >= 21

age = 20
age <= 20

# using 'and'
age_0 = 20
age_1 = 30
age_0 > 10 and age_1 < 30

(age_0 >= 20) and (age_1 >= 20)

# using 'or'
age_0 = 20
age_1 = 30
age_0 > 5 or age_1 < 10

# checking if value is is list
tops = ['chicken', 'chilli', 'tuna', 'tomotoes']
'tuna' in tops
'sweetcorn' in tops

user = 'sweetcorn'
if user not in tops:
    print(f"I do not like {user.title()}")

# simple if statement
age_3 = 205
if age_3 > 70:
    print('you are too old')

# if-else statement
age_3 = 205
if age_3 > 70:
    print('you are too old')
else:
    print("you are not too old yet")


# if-elif-else
age_4 = 4
if age < 4:
    print('$0')
elif age_4 < 18:
    print('$10')
else:
    print('$20')

AGE = 70
if AGE < 4:
    print('$0')
elif AGE < 18:
    print('$10')
elif AGE < 65:
    print('$20')
elif AGE >= 65:
    print('$10')

# testing multiple conditions
toppings = ['chicken', 'corn', 'tuna']

if 'chicken' in toppings:
    print('add chicken')
if 'corn' in toppings:
    print('add corn')
if 'chilli' in toppings:
    print('add chilli')

# ex 5-3
alien_colour = ['yellow', 'green', 'red']
if alien_colour[1] == 'green':
    print('add 5 points')

# using if statement with lists
# chebking for special items
toppings = ['chicken', 'corn', 'tuna']
for topping in toppings:
    print(f"adding {topping}\n")

toppings = ['chicken', 'corn', 'tuna']
for topping in toppings:
    if topping == 'corn':
        print(f'sorry we ran out of {topping}')
    else:
        print(f"adding{topping}")

# checkeing list is not empty
toppings = []
if toppings:
    for topping in toppings:
        print(f"adding {topping}")
    print('\n finished making your pizza')
else:
    print('plain pizza?')

# using multiple lists
toppings_A = ['chicken', 'tuna', 'mashrooms', 'olives', 'peppers']
toppings = ['chicken', 'corn', 'tuna']
for topping in toppings:
    if topping in toppings_A:
        print(f"adding {topping}")
    else:
        print(f"sorry, {topping} is not availale")
print(f"\n you're pizza is ready'")

# ex 5-8
usernames = ['admin', 'salman', 'ashraf', '2513', 'ali']
for username in usernames:
    if username == 'admin':
        print(f"hello {username}")
    else:
        print(f"hello {username}")

usernames = ['admin', 'salman', 'ashraf', '2513', 'ali']
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f"hello {username}")
        else:
            print(f"hello {username}")
else:
    print('not available')
