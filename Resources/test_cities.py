import unittest
from city_country import city_country


class CityTestCase(unittest.TestCase):
    """test for 'city_country.py'"""

    def test_city_country(self):
        """does string like 'london' and 'UK' work?"""
        result = city_country('London', 'UK', 100)
        self.assertEqual(result, 'London, UK - 100')


if __name__ == '__main___':
    unittest.main()
