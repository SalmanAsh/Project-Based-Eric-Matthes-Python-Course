# Functions
import pizza


def greet_user():
    """Display a simple greeting"""
    print("Hello")


greet_user()

# passing information to a function


def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username}")


greet_user('sal')

# ex 8-1


def favorite_book(title):
    """favorite book"""
    print(f"My favorte book is {title}")


favorite_book('none')

# positional arguments


def describe_pet(animal_type, pet_name):
    """Display information about an animal"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('dog', 'happy')

# multiple function calls


def describe_pet(animal_type, pet_name):
    """Display information about an animal"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('dog', 'happy')
describe_pet('cat', 'billy')

# keyword arguments


def describe_pet(animal_type, pet_name):
    """Display information about an animal"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(animal_type='dog', pet_name='billy')

# default values


def describe_pet(pet_name, animal_type='dog'):
    """Display information about an animal"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('billy')


def describe_pet(pet_name, animal_type='dog'):
    """Display information about an animal"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet(pet_name='billy', animal_type='cat')


def describe_pet(pet_name='billy', animal_type='dog'):
    """Display information about an animal"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet()

# equivalent function calls


def describe_pet(pet_name, animal_type='dog'):
    """Display information about an animal"""
    print(f"\nI have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}")


describe_pet('billy')
describe_pet(pet_name='billy')
describe_pet('billy', 'cat')
describe_pet(pet_name='billy', animal_type='cat')
describe_pet(animal_type='cat', pet_name='billy')

# ex8-4


def make_shirts(size, design):
    """shirt of size and certain design"""
    print(
        f"the shirt is {size} size and it should have the following text on it: {design}")


make_shirts('small', 'hello')
make_shirts(size='small', design='hello')


def describe_city(city, country='UK'):
    """A city of certain country"""
    print(f"{city.title()} is in {country.title()}")


describe_city('manchester')
describe_city(city='cairo', country='egypt')
describe_city(country='pakistan', city='mandi')

# returning a simple values


def get_formatted_name(first_name, last_name):
    """Return full name"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('salman', 'ashraf')
print(musician)

# making an argument optional


def get_formatted_name(first_name, middle_name, last_name):
    """Return full name"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('salman', 'codes', 'ashraf')
print(musician)


def get_formatted_name(first_name, last_name, middle_name=''):
    """Return full name"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()


musician = get_formatted_name('salman', 'ashraf')
print(musician)

musician = get_formatted_name('salman', 'ashraf', 'codes')
print(musician)

# returning a dictionary


def build_person(first_name, last_name, age=None):
    """return a dictionary with a person's info"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('salman', 'ashraf')
print(musician)

musician = build_person('salman', 'ashraf', 20)
print(musician)

# using the function with a while loop


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print('please tell me your name:')
    f_name = input("first name?")
    l_name = input("last name?")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")


def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()


while True:
    print('please tell me your name:')
    print('enter q to exit')
    f_name = input("first name?")
    if f_name == 'q':
        break
    l_name = input("last name?")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")

# ex 8-6


def make_album(artist_name, album_title):
    """describing a music album"""
    album = {'artist': artist_name, 'title': album_title}
    return album


music_0 = make_album('bohemia', '1000')
print(music_0)
music_1 = make_album('bohemia', 'skull&bones')
print(music_1)
music_2 = make_album('siddhu', '295')
print(music_2)


def make_album(artist_name, album_title, songs=None):
    """describing a music album"""
    album = {'artist': artist_name, 'title': album_title}
    if songs:
        album['songs'] = songs
    return album


music_0 = make_album('bohemia', '1000', 50)
print(music_0)
music_1 = make_album('bohemia', 'skull&bones')
print(music_1)
music_2 = make_album('siddhu', '295', 10)
print(music_2)


def make_album(artist_name, album_title, songs=None):
    """describing a music album"""
    album = {'artist': artist_name, 'title': album_title}
    if songs:
        album['songs'] = songs
    return album


while True:
    print('please enter the following info')
    print("or q to exit")
    a_name = input("artist name?")
    if a_name == 'q':
        break
    a_title = input('album title?')
    if a_title == 'q':
        break
    song = input("number of songs")
    if song == 'q':
        break
    music = make_album(a_name, a_title, song)
    print(music)

# passing a list


def greet_user(names):
    """print a greeting message"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)


usernames = ['salman', 'joe', 'ali']
greet_user(usernames)

# modifying the list in a funcion
unprinted_designs = ['phone case', 'screw', 'pen']
completed_models = []
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
print(f"\nThe following models are completed:")
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, ultil none left.
    Move each design in completed_model once finished
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show printed printed models"""
    print(f"\nThe following models are printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['phone case', 'screw', 'pen']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# preventing a function from modifying the list
print(unprinted_designs[:], completed_models)

# ex 8-9
messages = ['hi', 'hello', 'bye']


def short_messages(greets):
    """print a short message"""
    for greet in greets:
        print(greet)


short_messages(messages)


def send_messages(greets, sent_messages):
    while greets:
        greet = greets.pop()
        print(f"message sent: {greet}")
        sent_messages.append(greet)


greets = ['hi', 'hello', 'bye']
sent_messages = []

send_messages(greets, sent_messages)
print(sent_messages)


def send_messages(greets, sent_messages):
    while greets:
        greet = greets.pop()
        print(f"message sent: {greet}")
        sent_messages.append(greet)


greets = ['hi', 'hello', 'bye']
sent_messages = []

send_messages(greets[:], sent_messages)
print(greets)
print(sent_messages)

# passing an arbitrary number of arguments


def make_pizza(*toppings):
    """print a list of toppings"""
    for topping in toppings:
        print(topping)


make_pizza('papperoni')
make_pizza('mushroom', 'tuna', 'extra cheese')

# mixing positional and arbitrary argumants


def make_pizza(size, *toppings):
    """Give pizza size and toppings"""
    print(f"\nMake a {size} inch pizza and with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'tuna', 'chicken')

# using arbitrary keyword arguments


def build_profile(first, last, **userinfo):
    """build a dictionary containig info about user"""
    userinfo['first_name'] = first
    userinfo['last_name'] = last
    return userinfo


user_profile = build_profile(
    'salman', 'ashraf', location='manchester', field='cs')
print(user_profile)

# ex 8-12


def sandwich(*items):
    """Items in a sandwich"""
    print(f"Make a sanwich with the following items:")
    for item in items:
        print(item.title())


sandwich('tuna', 'egg', 'mayo')


def build_profile(first, last, **info):
    """about me"""
    info['first_name'] = first
    info['last_name'] = last
    return info


me = build_profile('salman', 'last', location='manchester',
                   field='cs', passion='cricket')
print(me)

# Storing function in modules
# importing an entire module
"""making a file pizza.py"""

"""import pizza"""
pizza.make_pizza(16, 'tuna')
pizza.make_pizza(12, 'tuna', 'chicken', 'tomatos')

# importing specific functions
"""from pizza import make_pizza"""
pizza.make_pizza(16, 'tuna')
pizza.make_pizza(12, 'tuna', 'chicken', 'tomatos')

# importing a function with a different name or alias
"""from pizza import make_pizza as mp"""
mp(16, 'tuna')
mp(12, 'tuna', 'chicken', 'tomatos')

# importing an entire module as an alias
"""import pizza as p"""
p.make_pizza(16, 'tuna')
p.make_pizza(12, 'tuna', 'chicken', 'tomatos')

# import all functions in a module
""" from pizza import * """
make_pizza(16, 'tuna')
make_pizza(12, 'tuna', 'chicken', 'tomatos')
