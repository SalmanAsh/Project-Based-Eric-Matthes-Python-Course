"""A class to represent an electric car"""


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
