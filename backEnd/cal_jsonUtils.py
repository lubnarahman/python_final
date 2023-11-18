import json
from backEnd.exceptions import InvalidMealException, BigMealException

def load_json_file(file_path):
    with open(file_path) as file:
        return json.load(file)

meals_data = load_json_file("data/meals.json")['meals']
combos_data = load_json_file("data/combos.json")['combos']

meal_dist_by_id = {meal["id"]: meal for meal in meals_data}
meal_dist_by_name = {meal["name"]: meal for meal in meals_data}
combo_dist_by_id = {combo["id"]: combo for combo in combos_data}
combo_dist_by_name = {combo["name"]: combo for combo in combos_data}

def comp_cal_counter_json(*list_of_items):
    total_calories = 0

    for item in list_of_items:
        try:
            if item in meal_dist_by_id:
                total_calories += meal_dist_by_id[item]['calories']
            elif item in meal_dist_by_name:
                total_calories += meal_dist_by_name[item]['calories']
            elif item in combo_dist_by_id:
                for combo_item in combo_dist_by_id[item]['meals']:
                    total_calories += meal_dist_by_id[combo_item]['calories']
            else:
                for combo_item in combo_dist_by_name[item]['meals']:
                    total_calories += meal_dist_by_id[combo_item]['calories']
        except KeyError:
            raise InvalidMealException(item)

    if total_calories > 2000:
        raise BigMealException(total_calories)

    return total_calories

def price_counter_json(*list_of_items):
    sum_price = 0
    combo_price = 0

    for item in list_of_items:
        try:
            if item in meal_dist_by_id:
                sum_price += meal_dist_by_id[item]['price']
            elif item in meal_dist_by_name:
                sum_price += meal_dist_by_name[item]['price']
            elif item in combo_dist_by_id:
                combo_price += combo_dist_by_id[item]['price']
                for combo_item in combo_dist_by_id[item]['meals']:
                    sum_price += meal_dist_by_id[combo_item]['price']
            else:
                combo_price += combo_dist_by_name[item]['price']
                for combo_item in combo_dist_by_name[item]['meals']:
                    sum_price += meal_dist_by_id[combo_item]['price']
        except KeyError:
            raise InvalidMealException(item)

    if combo_price == 0:
        return sum_price
    else:
        return combo_price
