import unittest
from chapter11.py import get_formatted_name


class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py"""

    def test_first_last_name(self):
        """do name like "Salman Ashraf' work?"""
        formatted_name = get_formatted_name('salman', 'ashraf')
        self.assertEqual(formatted_name, 'Salman Ashraf')


if __name__ == '__main__':
    unittest.main()
