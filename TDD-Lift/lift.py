import unittest


#lift : [[1,2],[2,3],[3,2]]

class LiftTest(unittest.TestCase):
    def test_input_1_and_position_1_should_return_lift1(self):
        expected = 'lift1'
        actual = lift(1, 1)
        self.assertEqual(actual, expected)

def lift(input, position):
    return 'lift1'

unittest.main()
