class MenuItem:
    def __init__(self, id, name, calories, price):
        self.id = id
        self.name = name
        self.calories = calories
        self.price = price

# Define individual meals
hamburger = MenuItem("meal-1", "Hamburger", 600, 5)
cheese_burger = MenuItem("meal-2", "Cheese Burger", 750, 7)
veggie_burger = MenuItem("meal-3", "Veggie Burger", 400, 6)
vegan_burger = MenuItem("meal-4", "Vegan Burger", 350, 6)
sweet_potatoes = MenuItem("meal-5", "Sweet Potatoes", 230, 3)
salad = MenuItem("meal-6", "Salad", 15, 4)
iced_tea = MenuItem("meal-7", "Iced Tea", 70, 2)
lemonade = MenuItem("meal-8", "Lemonade", 90, 2)

# Define combos using MenuItem instances
cheesy_combo = {"id": "combo-1", "name": "Cheesy Combo", "meals": [cheese_burger, sweet_potatoes, lemonade], "price": 11}
veggie_combo = {"id": "combo-2", "name": "Veggie Combo", "meals": [veggie_burger, sweet_potatoes, iced_tea], "price": 10}
vegan_combo = {"id": "combo-3", "name": "Vegan Combo", "meals": [vegan_burger, salad, lemonade], "price": 10}

# Create dictionaries for quick access to meals and combos by id and name
meal_dist_by_id = {meal.id: meal for meal in [hamburger, cheese_burger, veggie_burger, vegan_burger, sweet_potatoes, salad, iced_tea, lemonade]}
meal_dist_by_name = {meal.name.lower(): meal for meal in [hamburger, cheese_burger, veggie_burger, vegan_burger, sweet_potatoes, salad, iced_tea, lemonade]}
combo_dist_by_id = {combo["id"]: combo for combo in [cheesy_combo, veggie_combo, vegan_combo]}
combo_dist_by_name = {combo["name"].lower(): combo for combo in [cheesy_combo, veggie_combo, vegan_combo]}
