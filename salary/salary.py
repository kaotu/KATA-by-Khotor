import unittest
import datetime

class SalaryTest(unittest.TestCase):
    def test_input_day_5_Apr_to_1_Apr_should_return_error(self):
        start_date = datetime.datetime(2019, 4, 5)
        end_date = datetime.datetime(2019, 4, 1)
        expected = 'error'
        actual = salary_date_time(start_date, end_date)
        self.assertEqual(actual, expected)

    def test_input_day_1Apr_to_1_Apr_should_return_5_bath(self):
        start_date = datetime.datetime(2019, 4, 1)
        end_date = datetime.datetime(2019, 4, 5)
        expected = 5
        actual = salary_date_time(start_date, end_date)
        self.assertEqual(actual, expected)

def salary_date_time(start_date, end_date):
        #if  end_date.date() - start_date.date() <  0
        print(end_date.timedelta.days())
        return 'error'


unittest.main()
