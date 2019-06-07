import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_input_3_should_return_fizz(self):
        expected = 'fizz'
        actual = fizzbuzz(3)
        self.assertEqual(actual, expected)

    def test_input_5_should_return_buzz(self):
        expected = 'buzz'
        actual = fizzbuzz(5)
        self.assertEqual(actual, expected)

    def test_input_2_should_return_2(self):
        expected = 2
        actual = fizzbuzz(2)
        self.assertEqual(actual, expected)

    def test_input_6_should_return_fizz(self):
        expected = 'fizz'
        actual = fizzbuzz(6)
        self.assertEqual(actual, expected)

    def test_input_10_should_return_10(self):
        expected = 'buzz'
        actual = fizzbuzz(10)
        self.assertEqual(actual, expected)


def fizzbuzz(number):
    if number % 3 == 0:
        return 'fizz'
    elif number % 5 == 0:
        return 'buzz'
    return number


unittest.main()
