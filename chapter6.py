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
# list of dictionraries
alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yelloe', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}
aliens = [alien_0, alien_1, alien_2]
print(aliens)

alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yelloe', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print(f"total number of aliens: {len(aliens)}")

aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(alien)
    print("...")

# a list in a dictionary
pizza = {'crust': 'thick',
         'toppings': ['mushroom', 'extra cheese']
         }
print(f"You ordered a {pizza['crust']} crust pizza with {pizza['toppings']}")

pizza = {'crust': 'thick',
         'toppings': ['mushroom', 'extra cheese']
         }
print(f"\nYou ordered a {pizza['crust']} crust pizza with following toppings:")
for topping in pizza['toppings']:
    print(f"\t{topping}")

favorite_languages = {
    'salman': ['python', 'PHP'],
    'joe': ['english'],
    'ali': ['java', 'haskell'],
    'abdullah': ['python', 'java']
}
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favourite language is:")
    for language in languages:
        print(language)

# dictionary in a dictionary
users = {
    'joeh': {
        'name': 'joseph',
        'last': 'hayes',
        'location': 'didsbury'
    },
    'alim': {
        'name': 'ali',
        'last': 'mohammed',
        'location': 'gorton'
    },
    'salmana': {
        'name': 'salman',
        'last': 'ashraf',
        'location': 'rusholme'
    }
}
for user, users_info in users.items():
    print(f"\nUsername: {user}")
    for one, two in users_info.items():
        print(f"Full Name: {two[0]}{two[1]}")
        print(f"Location: {two[2]}")


users = {
    'joeh': {
        'name': 'joseph',
        'last': 'hayes',
        'location': 'didsbury'
    },
    'alim': {
        'name': 'ali',
        'last': 'mohammed',
        'location': 'gorton'
    },
    'salmana': {
        'name': 'salman',
        'last': 'ashraf',
        'location': 'rusholme'
    }
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['name'].title()} {user_info['last'].title()}"
    location = user_info['location'].title()
    print(f"Full_name= {full_name}")
    print(f"Location= {location}")

# ex 6-7
pet_1 = {'name': 'dog', 'color': 'black', 'age': 6}
pet_2 = {'name': 'cat', 'color': 'white', 'age': 2}
pet_3 = {'name': 'parrot', 'color': 'green', 'age': 1}
pets = [pet_1, pet_2, pet_3]
for pet in pets:
    print(pet)

Places = {
    'salman': ['morocco', 'usa', 'saudi'],
    'joe': ['pakistan', 'korea'],
    'ali': ['usa']
}
for name, place_s in Places.items():
    print(f"{name.title()}'s favourite places are:")
    for place in place_s:
        print(place)

cities = {
    'london': {
        'country': 'uk',
        'population': '36m',
        'fact': 'shit city'
    },
    'dubai': {
        'country': 'saudi',
        'population': '15m',
        'fact': 'tall city'
    }
}
for city, city_info in cities.items():
    print(f"\n-Here's some info about the city of {city.title()}:")
    Country = f"\t-The city is in {city_info['country']}."
    population = f"\t-It has population of {city_info['population']}."
    fact = f"\t-It is a fact that the city is {city_info['fact']}."
    print(Country)
    print(population)
    print(fact)
