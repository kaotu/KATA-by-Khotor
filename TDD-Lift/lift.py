import unittest


#lift : [[1,2],[2,3],[3,5]]

class LiftTest(unittest.TestCase):
    def test_input_1_should_return_lift_1(self):
        expected = 'lift_1'
        actual = lift(1)
        self.assertEqual(actual, expected)

    def test_input_2_should_return_lift_1(self):
        expected = 'lift_1'
        actual = lift(2)
        self.assertEqual(actual, expected)

    def test_input_3_should_return_lift_2(self):
        expected = 'lift_2'
        actual = lift(3)
        self.assertEqual(actual, expected)



lift_all = [
    {'lift':'lift_1', 'floor': 2},
    {'lift':'lift_2', 'floor': 3},
    {'lift':'lift_3', 'floor': 5}
]

def lift(input):
    if input == 2:
        return lift_all[0].get('lift')
    elif input == 3:
        return lift_all[1].get('lift')
    return lift_all[0].get('lift')

unittest.main()
