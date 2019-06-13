import unittest


#lift : [[1,2],[2,3],[3,2]]

class LiftTest(unittest.TestCase):
    def test_input_1_should_return_lift1(self):
        expected = 'lift1'
        actual = lift(1)
        self.assertEqual(actual, expected)

    def test_input_2_should_return_lift3(self):
        expected = 'lift3'
        actual = lift(2)
        self.assertEqual(actual, expected)

def lift(input):
    if input == 2:
        return 'lift3'
    return 'lift1'

unittest.main()
