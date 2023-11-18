from unittest import TestCase
from backEnd.utils import (
    calories_counter,
    comp_cal_counter,
    comp_cal_counter2,
    price_counter
)
from backEnd.jsonUtils import (
    comp_cal_counter_json,
    price_counter_json
)

class CalorieCounterTestCase(TestCase):

    def assertCalories(self, function, expected, *args):
        result = function(*args)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_calories_simple(self):
        self.assertCalories(calories_counter, 685, 'Hamburger', 'Salad', 'Iced Tea')

    def test_calories_combo(self):
        self.assertCalories(calories_counter, 1070, 'Cheesy Combo')

    def test_mix(self):
        self.assertCalories(calories_counter, 1670, 'Hamburger', 'Cheesy Combo')

    def test_calories_complex_id(self):
        self.assertCalories(comp_cal_counter, 1750, 'meal-1', 'meal-2', 'meal-3')

    def test_calories_complex_name(self):
        self.assertCalories(comp_cal_counter, 685, 'hamburger', 'salad', 'iced tea')

    def test_calories_combo_complex_id2(self):
        self.assertCalories(comp_cal_counter, 1770, 'combo-1', 'combo-2')

    def test_calories_combo_complex_name2(self):
        self.assertCalories(comp_cal_counter, 1770, 'cheesy combo', 'veggie combo')

    def test_calories_complex_mix_id2(self):
        self.assertCalories(comp_cal_counter, 1300, 'meal-1', 'combo-2')

    def test_calories_complex_mix_name2(self):
        self.assertCalories(comp_cal_counter, 1300, 'hamburger', 'veggie combo')

    def test_calories_combo_complex_id(self):
        self.assertCalories(comp_cal_counter2, 1770, 'combo-1', 'combo-2')

    def test_calories_combo_complex_name(self):
        self.assertCalories(comp_cal_counter2, 1770, 'cheesy combo', 'veggie combo')

    def test_calories_complex_mix_id(self):
        self.assertCalories(comp_cal_counter2, 1300, 'meal-1', 'combo-2')

    def test_calories_complex_mix_name(self):
        self.assertCalories(comp_cal_counter2, 1300, 'hamburger', 'veggie combo')


class PriceCounterTestCase(TestCase):

    def assertPrice(self, expected, *args):
        result = price_counter(*args)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_price_complex_id(self):
        self.assertPrice(18, 'meal-1', 'meal-2', 'meal-3')

    def test_price_complex_name(self):
        self.assertPrice(11, 'hamburger', 'salad', 'iced tea')


class JsonFileTestCase(TestCase):

    def assertJsonFile(self, function, expected, *args):
        result = function(*args)
        self.assertEqual(result, expected, f"Expected {expected}, got {result}")

    def test_json_calories_combo_complex_id(self):
        self.assertJsonFile(comp_cal_counter_json, 1770, 'combo-1', 'combo-2')

    def test_json_calories_combo_complex_name(self):
        self.assertJsonFile(comp_cal_counter_json, 1770, 'cheesy combo', 'veggie combo')

    def test_json_calories_complex_mix_id(self):
        self.assertJsonFile(comp_cal_counter_json, 1300, 'meal-1', 'combo-2')

    def test_json_calories_complex_mix_name(self):
        self.assertJsonFile(comp_cal_counter_json, 1300, 'hamburger', 'veggie combo')

    def test_json_price_complex_id(self):
        self.assertJsonFile(price_counter_json, 18, 'meal-1', 'meal-2', 'meal-3')

    def test_json_price_complex_name(self):
        self.assertJsonFile(price_counter_json, 11, 'hamburger', 'salad', 'iced tea')
