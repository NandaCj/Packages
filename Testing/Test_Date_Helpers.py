import unittest
from Date_Helpers import Date_Helpers
import datetime

Test_Date = '01-Jan-2018'
DH = Date_Helpers(Test_Date)

class Test_Date_Helpers(unittest.TestCase):
    """
    This tests the Date_helpers module
    """
    def setUp(self):
        pass

    def test_string_to_dt_object(self):
        date = DH.string_to_dt_object
        self.assertEqual(date.year, 2018)
        self.assertEqual(date.day, 1)
        self.assertEqual(date.month, 1)


if __name__ == '__main__':
   unittest.main()