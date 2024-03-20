import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    '''test name_function.py'''
    def test_first_last_name(self):
        '''Can a name like Janis Joplin be processed correctly?'''
        formatted_name = get_formatted_name('janis','joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
    def test_first_last_middle_name(self):
        """ Can a namelike Wolfgang Amadeus Mozart be processed correctly? """
        formatted_name = get_formatted_name('Wolfgang','Mozart','Amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

