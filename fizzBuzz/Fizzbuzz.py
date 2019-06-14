import unittest


fizz = 'fizz'
buzz = 'buzz'
fizzbuzz = 'fizzbuzz'

class FizzBuzzTest(unittest.TestCase):

    def test_input_3_sholud_return_fizz(self):
        expected = fizz
        actual = fizz_buzz(3)
        self.assertEqual(actual, expected)

    def test_input_5_should_return_buzz(self):
        expected = buzz
        actual = fizz_buzz(5)
        self.assertEqual(actual, expected)

    def test_input_1_should_return_1(self):
        expected = 1
        actual = fizz_buzz(1)
        self.assertEqual(actual, expected)

    def test_input_6_should_return_fizz(self):
        expected = fizz
        actual = fizz_buzz(6)
        self.assertEqual(actual, expected)

    def test_input_10_should_return_buzz(self):
        expected = buzz
        actual = fizz_buzz(10)
        self.assertEqual(actual, expected)

    def test_input_15_should_return_fizzbuzz(self):
        expected = fizzbuzz
        actual = fizz_buzz(15)
        self.assertEqual(actual, expected)

    def test_input_30_should_return_fizzbuzz(self):
        expected = fizzbuzz
        actual = fizz_buzz(30)
        self.assertEqual(actual, expected)


def fizz_buzz(number):
    result = {
        number: True,
        number % 3 == 0: fizz,
        number % 5 == 0: buzz,
        number % 15 == 0: fizzbuzz
    }
    return result.get(True)


unittest.main()
