class BigMealException(Exception):
    def __init__(self, calories):
        message = f"Meal has {calories} calories, which is too much!"
        super().__init__(message)

class InvalidMealException(Exception):
    def __init__(self, item):
        message = f"Meal {item} is invalid!"
        super().__init__(message)
