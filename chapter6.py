# Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

# accessing a value
alien_0 = {'color': 'green', 'points': 5}
new_point = alien_0['points']
print(f"you have earned {new_point}")

# adding new key-value pair
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_positions'] = 25
print(alien_0)

# modifying values
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['color'] = 'yellow'
print(alien_0)


alien_0 = {'x_position': 0, 'y_positions': 25, 'speed': 'medium'}
print(f"original position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0['x_position'])

# removing key-value pair
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

# more dictionraries
favorite_languages = {
    'salman': 'python',
    'joe': 'english',
    'ali': 'java',
    'abdullah': 'php'
}
print(f"joe's favourite language is {favorite_languages['joe'].title()}")

# using get()
alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0.get('points', 'no points assigned'))

# ex 6-1
joe = {'first_name': 'joe', 'last_name': 'hayes',
       'age': 19, 'city': 'manchester'}
print(joe['first_name'])
print(joe['last_name'])
print(joe['age'])
print(joe['city'])

# looping through all key-value pair
user_0 = {'username': 'salman.ashraf2513', 'first': 'salman', 'last': 'ashraf'}
for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"\nvalue: {value}")

favorite_languages = {
    'salman': 'python',
    'joe': 'english',
    'ali': 'java',
    'abdullah': 'php'
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")

# looping through all the keys
favorite_languages = {
    'salman': 'python',
    'joe': 'english',
    'ali': 'java',
    'abdullah': 'php'
}
for name in favorite_languages.keys():
    print(name.title())

favorite_languages = {
    'salman': 'python',
    'joe': 'english',
    'ali': 'java',
    'abdullah': 'php'
}
friends = ['joe', 'ali']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        print(
            f"{name.title()}, I see you like {favorite_languages[name].title()}")

favorite_languages = {
    'salman': 'python',
    'joe': 'english',
    'ali': 'java',
    'abdullah': 'php'
}
if 'sikandar' not in favorite_languages.keys():
    print('sikandar did not take the poll')

# looping in a particular order
favorite_languages = {
    'salman': 'python',
    'joe': 'english',
    'ali': 'java',
    'abdullah': 'php'
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")

# looping through the values
favorite_languages = {
    'salman': 'python',
    'joe': 'english',
    'ali': 'java',
    'abdullah': 'php'
}
print("languages mentioned:")
for language in favorite_languages.values():
    print(language.title())

# using set() to avoid repetitions
favorite_languages = {
    'salman': 'python',
    'joe': 'english',
    'ali': 'java',
    'abdullah': 'python'
}
print("languages mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# ex 6-4
programming_words = {
    'get': 'assigns a default value',
    'sorted': 'tamporary sort the list',
    'sort': 'permanently sort the list',
    'set': 'finds uniques values only',
    'if': 'condition test'
}
for word, meaning in programming_words.items():
    print(f"key word {word} means {meaning}")

rivers = {'po': 'italy', 'thames': 'uk', 'nile': 'egypt'}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

rivers = {'po': 'italy', 'thames': 'uk', 'nile': 'egypt'}
print(rivers.keys())
print(rivers.values())
for river in rivers.keys():
    print(river)
for country in rivers.values():
    print(country)

# nesting
