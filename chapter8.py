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
