# the __init() method
class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate a dog rolling in response to a command"""
        print(f"{self.name} is now rolled over")

# accessing attributes


class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate a dog rolling in response to a command"""
        print(f"{self.name} is now rolled over")


my_dog = Dog('bill', 5)
print(my_dog.name)
print(my_dog.age)

# calling methods


class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate a dog rolling in response to a command"""
        print(f"{self.name} is now rolled over")


my_dog = Dog('bill', 5)
my_dog.sit()
my_dog.roll_over()

# creating multiple instances


class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """simulate a dog rolling in response to a command"""
        print(f"{self.name} is now rolled over")


my_dog = Dog('bill', 6)
your_dog = Dog('billy', 5)

print(f"name: {my_dog.name}")
print(f"age: {my_dog.age}")
my_dog.roll_over()

print(f"name: {your_dog.name}")
print(f"age: {your_dog.age}")
my_dog.sit()

# ex 9-1


class Restaurant:
    """Restaurant info"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(
            f"the restaurant name is {restaurant_name} and it offers {cuisine_type} cuisines")

    def open_restaurant(self):
        print("open")


restaurant = Restaurant('ibos', 'kebab')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)


class User:
    """User info"""

    def __init__(self, first_name, last_name, age, location):
        self.first = first_name
        self.last = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print(f"Name: {self.first} {self.last}")
        print(f"Age: {self.age}")
        print(f'location: {self.location}')

    def greet_user(self):
        print(f"Hello, Mr {self.first}")


customer_1 = User('salman', 'ashraf', '20', 'manchester')
print(customer_1.age)


# the car class
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """return a neatlt formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car('opel', model='corsa', year=2003)
print(my_new_car.get_descriptive_name())


# setting a default value for an attribute
