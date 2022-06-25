class User:
    """User info"""

    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def describe_user(self):
        print(f"Name: {first_name}")

    def greet_user(self):
        print(f"Hello, Mr {first_name}")


customer = User('salman', 'ashraf')
print(customer.describe_user())
