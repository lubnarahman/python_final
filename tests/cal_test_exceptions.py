from unittest import TestCase
from backEnd.utils import calories_counter, comp_cal_counter, comp_cal_counter2
from backEnd.exceptions import BigMealException

class BigMealTestCase(TestCase):

    def assertBigMealException(self, function, *args):
        with self.assertRaises(BigMealException) as e:
            function(*args)
            self.assertEqual(
                e.exception.message,
                "Meal has 3210 calories, which is too much!",
                "Wrong exception message"
            )

    def test_calories_counter_exception(self):
        self.assertBigMealException(calories_counter, 'Cheesy Combo', 'Cheesy Combo', 'Cheesy Combo')

    def test_comp_cal_counter_exception(self):
        self.assertBigMealException(comp_cal_counter, 'combo-1', 'combo-1', 'combo-1')

    def test_comp_cal_counter2_exception(self):
        self.assertBigMealException(comp_cal_counter2, 'combo-1', 'combo-1', 'combo-1')
