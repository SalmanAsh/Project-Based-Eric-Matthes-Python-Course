# Lists
bicycles = ['my', 'name', 'is', 'salman', 'ashraf']
print(bicycles[0].title())
print(bicycles[1].title())
print(bicycles[2].title())
print(bicycles[3].title())
print(bicycles[4].title())
print(bicycles[-1].title())

message = f"{bicycles[0].title()} first name {bicycles[2]} {bicycles[3].title()}"
print(message)


# modifying lists
names = ['Sajjad', 'Joe', 'Hassan', 'Abdullah', 'Sikandar', 'Mohammed']
print(names)

names[2] = 'Dur-e'
print(names)


# Adding elements to the lists
friends = ['Sajjad', 'Hassan', 'Abdullah', 'Sikandar', 'Mohammed']
print(friends)

friends.append('Joseph')
print(friends)

Bros = []
Bros.append('Joe')
Bros.append('Abdullah')
Bros.append('Sajjad')
Bros.append('Mohammed')
Bros.append('Sikandar')
print(Bros)

Bros.insert(1, 'Alhaji')
print(Bros)

# Romving an item from a list

comp_Sci = ['Year 0', 'Year 1', 'Year 2', 'Year 3']
print(comp_Sci)

del comp_Sci[0]
comp_Sci.insert(2, 'Placement')
print(comp_Sci)

comp = ['Year 0', 'Year 1', 'Year 2', 'Year 3']
popped_comp = comp.pop(0)
print(comp)
info = f"{popped_comp} done"
print(info)

BSC = ['Year 0', 'Year 1', 'Year 2', 'Year 3']
DONE = 'Year 0'
BSC.remove('Year 0')
print(f"I have just finished {DONE}")

# Exersizes
guests = ['Sajjad', 'Hassan', 'Sikandar']
Cannot_Make_it = guests.pop(1)
print(f"Cannot come: {Cannot_Make_it}")
guests.insert(1, 'Joe')
print(f"Hello {guests[0].title()}, I would like to invite you to my party.")
print(f"Hello {guests[1].title()}, I would like to invite you to my party.")
print(f"Hello {guests[2].title()}, I would like to invite you to my party.")


# sorting Lists
cars = ['maserati', 'golf', 'toyota', 'fiat']
cars.sort()
print(cars)

car = ['yahama', 'audi', 'jaguar', 'bmw']
car.sort(reverse=True)
print(car)

plane = ['easyjet', 'ryanair', 'saudi', 'gulf']
print(plane)
print(sorted(plane))
print(plane)

# Print in reverse order
print(reversed(plane))
print(plane)
plane.reverse()
print(plane)

# Finding length of a list
len(plane)

# Exersize 3-8
places = ['egypt', 'saudi', 'morocco', 'turkey', 'pakistan']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
