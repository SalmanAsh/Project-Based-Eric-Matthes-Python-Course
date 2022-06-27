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
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0

    def get_descriptive_name(self):
        """return a neatlt formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometre(self):
        """print a statement showing car's mileage"""
        print(f"The car has {self.odometre_reading} miles on it")


my_new_car = Car(make='open', model='corsa', year=2003)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometre()


# modifying an attibute value directly

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0

    def get_descriptive_name(self):
        """return a neatlt formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometre(self):
        """print a statement showing car's mileage"""
        print(f"The car has {self.odometre_reading} miles on it")


my_new_car = Car(make='open', model='corsa', year=2003)
print(my_new_car.get_descriptive_name())
my_new_car.odometre_reading = 23
my_new_car.read_odometre()

# modifying an attibute value through a method


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0

    def get_descriptive_name(self):
        """return a neatlt formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometre(self):
        """print a statement showing car's mileage"""
        print(f"The car has {self.odometre_reading} miles on it")

    def update_odometre(self, mileage):
        """Update the odometer"""
        self.odometre_reading = mileage


my_new_car = Car(make='open', model='corsa', year=2003)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometre(23)
my_new_car.read_odometre()


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0

    def get_descriptive_name(self):
        """return a neatlt formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometre(self):
        """print a statement showing car's mileage"""
        print(f"The car has {self.odometre_reading} miles on it")

    def update_odometre(self, mileage):
        """Update the odometer"""
        """Reject any request to roll back the odometer"""
        if mileage >= self.odometre_reading:
            self.odometre_reading = mileage
        else:
            print("Error")


my_new_car = Car(make='open', model='corsa', year=2003)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometre(23)
my_new_car.read_odometre()

my_old_car = Car(make='opel', model='corsa', year=2001)
print(my_old_car.get_descriptive_name())
my_old_car.update_odometre(100000)
my_old_car.read_odometre()
my_old_car.update_odometre(50)
my_old_car.read_odometre()

# incrementing an attributes value through a method


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 50

    def get_descriptive_name(self):
        """return a neatlt formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometre(self):
        """print a statement showing car's mileage"""
        print(f"The car has {self.odometre_reading} miles on it")

    def increment_odometre(self, miles):
        """Update the odometer"""
        self.odometre_reading += miles


my_new_car = Car(make='open', model='corsa', year=2003)
print(my_new_car.get_descriptive_name())

my_new_car.increment_odometre(50)
my_new_car.read_odometre()


# inheritance

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0

    def get_descriptive_name(self):
        """return a neatlt formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometre(self):
        """print a statement showing car's mileage"""
        print(f"The car has {self.odometre_reading} miles on it")

    def update_odometre(self, mileage):
        """Update the odometer"""
        """Reject any request to roll back the odometer"""
        if mileage >= self.odometre_reading:
            self.odometre_reading = mileage
        else:
            print("Error")


class ElectricCar(Car):
    """Represent aspects of an electric car"""

    def __init__(self, make, model, year):
        """initialize attributes"""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', year=2019)
print(my_tesla.get_descriptive_name())

# defining addional attributes and methods for child class


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0

    def get_descriptive_name(self):
        """return a neatlt formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometre(self):
        """print a statement showing car's mileage"""
        print(f"The car has {self.odometre_reading} miles on it")

    def update_odometre(self, mileage):
        """Update the odometer"""
        """Reject any request to roll back the odometer"""
        if mileage >= self.odometre_reading:
            self.odometre_reading = mileage
        else:
            print("Error")


class ElectricCar(Car):
    """Represent aspects of an electric car"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        """print battery"""
        print(f"This car has a {self.battery_size}-kWh battery")


my_tesla = ElectricCar('tesla', 'model s', year=2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# overriding a method in child class
class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0

    def get_descriptive_name(self):
        """return a neatlt formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

        def fill_gas_tank(self):
            print("the car has a gas tank")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def fill_gas_tank():
        print("electric car do not have a gas tank")

# instances as attributes


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0

    def get_descriptive_name(self):
        """return a neatlt formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometre(self):
        """print a statement showing car's mileage"""
        print(f"The car has {self.odometre_reading} miles on it")

    def update_odometre(self, mileage):
        """Update the odometer"""
        """Reject any request to roll back the odometer"""
        if mileage >= self.odometre_reading:
            self.odometre_reading = mileage
        else:
            print("Error")


class Battery:
    """Electric car's battery"""

    def __init__(self, battery_size=85):
        """Initialize attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")


class ElectricCar(Car):
    """Electric car feature"""

    def __init__(self, make, model, year):
        """initialize Attributes"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', year=2019)
my_tesla.battery.describe_battery()


class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometre_reading = 0

    def get_descriptive_name(self):
        """return a neatlt formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometre(self):
        """print a statement showing car's mileage"""
        print(f"The car has {self.odometre_reading} miles on it")

    def update_odometre(self, mileage):
        """Update the odometer"""
        """Reject any request to roll back the odometer"""
        if mileage >= self.odometre_reading:
            self.odometre_reading = mileage
        else:
            print("Error")


class Battery:
    """Electric car's battery"""

    def __init__(self, battery_size=85):
        """Initialize attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """battery size"""
        print(f"This car has a {self.battery_size}-kWh battery")

    def get_range(self):
        """Print a statement about the range"""
        if self.battery_size == 75:
            range = 260
            print(f"This car can go about {range} miles on full charge")
        elif self.battery_size == 80:
            range = 315
            print(f"This car can go about {range} miles on full charge")


class ElectricCar(Car):
    """Electric car feature"""

    def __init__(self, make, model, year):
        """initialize Attributes"""
        super().__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', year=2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
