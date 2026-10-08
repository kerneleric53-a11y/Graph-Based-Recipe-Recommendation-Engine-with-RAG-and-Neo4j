# recipe_logic.py
def filter_by_ingredient(recipes, ingredient):
    return [r for r in recipes if ingredient in r['ingredients']]

def filter_by_cuisine(recipes, cuisine):
    return [r for r in recipes if r['cuisine'] == cuisine]

def filter_by_time(recipes, max_minutes):
    return [r for r in recipes if r['time'] <= max_minutes]