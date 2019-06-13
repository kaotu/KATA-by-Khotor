import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_input_5_should_return_buzz(self):
        expected = 'buzz'
        actual = fizz_buzz(5)
        self.assertEqual(actual, expected)

    def test_input_4_should_return_4(self):
        expected = 4
        actual = fizz_buzz(4)
        self.assertEqual(actual, expected)

    def test_input_15_should_return_fizzbuzz(self):
        expected = 'fizzbuzz'
        actual = fizz_buzz(15)
        self.assertEqual(actual, expected)

    def test_input_7_should_return_whoof(self):
        expected = 'whoof'
        actual = fizz_buzz(7)
        self.assertEqual(actual, expected)

    def test_input_divided_by_3_should_return_fizz(self):
        expected = 'fizz'
        actual = fizz_buzz(3)
        actual_2 = fizz_buzz(6)
        actual_3 = fizz_buzz(9)

        self.assertEqual(actual, expected)
        self.assertEqual(actual_2, expected)
        self.assertEqual(actual_3, expected)

def fizz_buzz(number):
    result = {
        True: number,
        number % 3 == 0: 'fizz',
        number % 5 == 0: 'buzz',
        number % 15 == 0: 'fizzbuzz',
        number == 7: 'whoof'
    }
    return result.get(True)


unittest.main()
