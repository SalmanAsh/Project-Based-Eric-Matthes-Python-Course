# for loops
cars = ['yahama', 'audi', 'jaguar', 'bmw']
for car in cars:
    print(car)

for car in cars:
    print(f"{car.title()} is my favourite car\n")

for car in cars:
    print(f"{car.title()} is my favourite car")
    print(f"\tbut i do not have enough money to buy a {car.title()}\n")

for car in cars:
    print(f"{car.title()} is my favourite car")
    print(f"\tbut i do not have enough money to buy a {car.title()}\n")
print('final result: I am too rich\n')

# Exersizes 4-1
pizzas = ['checken', 'vegetable', 'spicy']
for pizza in pizzas:
    print(f"i like {pizza} pizza")
print('i really love pizza')

# Using range funcion
for value in range(1, 5):
    print(value)

for values in range(6):
    print(values)

numbers = list(range(1, 6))
print(numbers)

even_numbers = list(range(2, 11, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

Squares = []
for value in range(1, 11):
    Squares.append(value ** 2)
print(Squares)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
sum(digits)

# list comprehension
poliname = [value**2 for value in range(1, 11)]
print(poliname)

# ex 4-3
for numbers in range(1, 21):
    print(numbers)

million = list(range(1, 10))
print(million)

print(min(million))
print(max(million))
print(sum(million))

odd_numbers = list(range(1, 20, 2))
print(odd_numbers)

for values in range(3, 31, 3):
    print(values)

for values in range(1, 11):
    print(values ** 3)

cubes = [values**3 for values in range(1, 11)]
print(cubes)

# Slicing a list
players = ['salman', 'sharaz', 'shamir', 'zain', 'talha']
print(players[0:3])
print(players[2:5])
print(players[:5])
print(players[2:])
print(players[-3:])

# looping through a slice
players = ['salman', 'sharaz', 'shamir', 'zain', 'talha']
for player in players[:3]:
    print(player.title())

# copying a list
my_food = ['pizza', 'pasta', 'lasagna', 'rise', 'chicken']
friend_food = my_food[:]
print(f"my favourite foods are {my_food}")
print(f"my friend's favoirite foods are {friend_food}")

# ex 4-10
Food = ['pizza', 'pasta', 'lasagna', 'rise', 'chicken']
print(Food[:3])
print(Food[-3:])

# tuples
dimensions = (200, 50)
print(dimensions)
print(dimensions[:])
print(dimensions[0])
print(dimensions[1])

# looping through a tuple
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

dimensions = (200, 50)
print('original dimensions:')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('modified dimensions:')
for dimension in dimensions:
    print(dimension)

# ex 4-13
buffets = ('chicken', 'naans', 'lamb', 'daal', 'sauces')
for buffet in buffets:
    print(buffet)
