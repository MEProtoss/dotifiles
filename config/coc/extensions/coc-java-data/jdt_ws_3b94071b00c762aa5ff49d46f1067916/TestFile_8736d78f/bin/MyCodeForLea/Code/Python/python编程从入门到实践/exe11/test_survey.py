import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Testing for TestAnonymousSurvey class"""

    def setUp(self):
        """Create a survey subject and a set of answers for each test to use"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']

    def test_store_single_response(self):
        """Testing individual answers will be properly stored"""
        self.my_survey.store_response('English')
        self.assertIn('English',self.my_survey.responses)

    def test_store_three_responses(self):
        """Testing three answers will be properly stored"""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()
        

