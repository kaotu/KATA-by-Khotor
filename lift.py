import unittest


#lift : [[1,2],[2,3],[3,2]]

class LiftTest(unittest.TestCase):
    def test_input_1_and_position_1_should_return_lift1(self):
        expected = 'lift1'
        actual = lift(1, 1)
        self.assertEqual(actual, expected)

    def test_input_1_and_position_3_sholud_return_lift3(self):
        expected = 'lift3'
        actual = lift(1, 1)
        self.assertEqual(actual, expected)

def lift(input, position):
    if input == 1 and position == 1:
        return 'lift1'
    return 'lift3'

unittest.main()
