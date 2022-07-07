import unittest
from survey import AnonymousSurvey


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
