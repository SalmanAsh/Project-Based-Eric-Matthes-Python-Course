"""A class to represent a car"""


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

    def increment_odometre(self, miles):
        """Update the odometer"""
        self.odometre_reading += miles


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
