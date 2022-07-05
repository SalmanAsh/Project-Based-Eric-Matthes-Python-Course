# Testing your code
# testing a function


from practice import get_formatted_name
import unittest


def get_formatted_name(first, last):
    """Generate a full name"""
    full_name = f"{first} {last}"
    return full_name.title()


print("Enter q to exit")
while True:
    first = input("\nPlease give first name")
    if first == 'q':
        break
    last = input("Please give second name")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(formatted_name)

# unit test and test cases
"""
class NameTestCase(unittest.TestCase):
    #Tests for 'name_function.py

    def test_first_last_name(self):
        #do name like "Salman Ashraf' work?
        formatted_name = get_formatted_name('salman', 'ashraf')
        self.assertEqual(formatted_name, 'Salman Ashraf')


if __name__ == '__main__':
    unittest.main()
"""
