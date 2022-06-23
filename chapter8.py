# Functions
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
