import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_input_3_should_return_fizz(self):
        expected = 'fizz'
        actual = fizzbuzz(3)
        self.assertEqual(expected, actual)

    def test_input_5_should_return_buzz(self):
        expected = 'buzz'
        actual = fizzbuzz(5)
        self.assertEqual(expected, actual)

    def test_input_7_shuold_return_7(self):
        expected = 7
        actual = fizzbuzz(7)
        self.assertEqual(expected, actual)

    def test_input_15_should_return_fizzbuzz(self):
        expected = 'fizzbuzz'
        actual = fizzbuzz(15)
        self.assertEqual(expected, actual)

    def test_input_30_should_return_fizzbuzz(self):
        expected = 'fizzbuzz'
        actual = fizzbuzz(30)
        self.assertEqual(expected, actual)

    def test_input_0_should_return_0(self):
        expected = 0
        actual = fizzbuzz(0)
        self.assertEqual(expected, actual)


def fizzbuzz(number):
    if number == 0:
        return 0
    elif number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    elif number % 5 == 0:
        return 'buzz'
    elif number % 3 == 0:
        return 'fizz'
    return number

unittest.main()
