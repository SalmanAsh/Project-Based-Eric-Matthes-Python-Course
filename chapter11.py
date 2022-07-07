# Testing your code
# testing a function

from survey import AnonymousSurvey


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

"""
class NameTestCase(unittest.TestCase):
    #Tests for 'name_function.py

    def test_first_last_name(self):
        #do name like "Salman Ashraf' work?
        formatted_name = get_formatted_name('salman', 'ashraf')
        self.assertEqual(formatted_name, 'Salman Ashraf')
    
        def test_first_middle_last_name(self):
        #Do names like 'salman codes ashraf' work?
        formatted_name=get_formatted_name('salman','codes', 'ashraf')
        self.assertEqual(formatted_name, 'Salman Codes Ashraf')

if __name__ == '__main__':
    unittest.main()
"""

# ex 11-1
"""
import unittest
from city_country import city_country


class CityTestCase(unittest.TestCase):
    #test for 'city_country.py'

    def test_city_country(self):
        #does string like 'london' and 'UK' work?
        result = city_country('London', 'UK')
        self.assertEqual(result, 'London, UK')
if __name__=='__main___':
    unittest.main()
"""

"""
import unittest
from city_country import city_country


class CityTestCase(unittest.TestCase):
    #test for 'city_country.py'

    def test_city_country(self):
        #does string like 'london' and 'UK' work?
        result = city_country('London', 'UK', 100)
        self.assertEqual(result, 'London, UK - 100')


if __name__ == '__main___':
    unittest.main()
"""

# testing a class


class AnonymousSurvey:
    """Collect answers to survey questions"""

    def __init__(self, question):
        """store a question, prepare to store an answer"""
        self.question = question
        self.responces = []

    def show_question(self):
        """Show survey question"""
        print(self.question)

    def store_responce(self):
        """store a single responce"""
        self.responces.append(new_responce)

    def show_result(self):
        """show all responces"""
        print("Survey Results:")
        for responce in responces:
            print(f" -{responce}")


"""Define a question, and make a survey"""
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

"""show the question and store responces to the question"""
my_survey.show_question()
print("Enter q to quit")
while True:
    responce = input("Language: ")
    if responce == 'q':
        break
    my_survey.store_responce(responce)

"""Show results"""
print("Thank you for participating")
my_survey.show_result()


# testing the class

"""
import unittest
from survey import AnonymousSurvey
"""


class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class"""

    def test_store_single_responce(self):
        """Test that a single responce in stored"""
        question = "What language did you first learn to speak?"""
        my_survey = AnonymousSurvey(question)
        my_survey.store_responce('english')
        self.assertIn('english', my_survey.responces)


if __name__ == '__main__':
    unittest.main()
