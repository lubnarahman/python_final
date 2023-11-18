from backEnd.constants import calories, combos, meals, combos2, meal_dist_by_id, meal_dist_by_name, combo_dist_by_id, combo_dist_by_name
from backEnd.exceptions import InvalidMealException, BigMealException

def calories_counter(*args):
    total_calories = 0

    for item in args:
        try:
            if item in calories:
                total_calories += calories[item]
            else:
                for combo_item in combos[item]:
                    total_calories += calories[combo_item]

        except KeyError:
            raise InvalidMealException(item)

    if total_calories > 2000:
        raise BigMealException(total_calories)

    return total_calories

def comp_cal_counter(*args):
    total_calories = 0

    for item in args:
        for meal in meals:
            if item == meal['id'] or item == meal['name']:
                total_calories += meal['calories']

        for combo in combos2:
            if item == combo['id'] or item == combo['name']:
                for mealInCombo in combo['meals']:
                    for meal in meals:
                        if mealInCombo == meal['id']:
                            total_calories += meal['calories']

    if total_calories > 2000:
        raise BigMealException(total_calories)

    return total_calories

def comp_cal_counter2(*list_of_items):
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

def price_counter(*list_of_items):
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
