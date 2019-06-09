import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_input_3_should_return_fizz(self):
        expected = 'fizz'
        actual = fizz_buzz(3)
        self.assertEqual(expected, actual)
        
    def test_input_5_should_return_buzz(self):
        expected = 'buzz'
        actual = fizz_buzz(5)
        self.assertEqual(expected, actual)
    
    def test_input_2_should_return_2(self):
        expected = 2
        actual = fizz_buzz(2)
        self.assertEqual(expected, actual)
    
    def test_input_30_should_return_fizzbuzz(self):
        expected = 'fizzbuzz'
        actual = fizz_buzz(30)
        self.assertEqual(expected, actual)

    def test_input_15_should_return_fizzbuzz(self):
        expected = 'fizzbuzz'
        actual = fizz_buzz(15)
        self.assertEqual(expected, actual)
        
        
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return 'fizzbuzz'
    elif number % 5 == 0:
        return 'buzz'
    elif number % 3 == 0:
        return 'fizz'        
    return number
    
    
unittest.main()