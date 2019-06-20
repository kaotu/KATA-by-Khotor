import unittest
import datetime


class SalaryTest(unittest.TestCase):
    def test_input_startdate_morethan_enddate_should_return_error(self):
        expected = 'error'

        start_date = datetime.datetime(2000, 4, 5)
        end_date = datetime.datetime(2000, 4, 1)
        actual = income(start_date, end_date)

        self.assertEqual(actual, expected)

    def test_should_get_1_baht_per_day_on_july(self):
        expected = 7

        start_date = datetime.datetime(2000, 7, 5)
        end_date = datetime.datetime(2000, 7, 11)
        actual = income(start_date, end_date)

        self.assertEqual(actual, expected)

    def test_should_get_100_baht_per_day_on_may(self):
        expected = 500

        start_date = datetime.datetime(2000, 5, 1)
        end_date = datetime.datetime(2000, 5, 5)
        actual = income(start_date, end_date)

        self.assertEqual(actual, expected)

    def test_should_get_100_bath_per_day_on_june(self):
        expected = 1000

        start_date = datetime.datetime(2000, 6, 10)
        end_date = datetime.datetime(2000, 6, 19)
        actual = income(start_date, end_date)

        self.assertEqual(actual, expected)

    def test_should_get_202_bath_from_different_mouth(self):
        expected = 202
        start_date = datetime.datetime(2000, 8, 30)
        end_date = datetime.datetime(2000, 9, 2)
        actual = income(start_date, end_date)

        self.assertEqual(actual, expected)


def income(start_date, end_date):
    day = (end_date.day - start_date.day)+1
    day_start = (31 - start_date.day)+1
    day_end = (day*(-1) - day_start)+1
    day = day_start

    if day < 0:
        return 'error'
    elif start_date.month == 5 or start_date.month == 6:
        return (day)*100
    elif end_date.month == 9:
        day_end *= 100
        day += day_end
        return day
    return day


unittest.main()
