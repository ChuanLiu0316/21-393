BREAKFAST = 'B'
LUNCH = 'L'
DINNER = 'D'

from reader import read_csv
from copy import copy

class Food(object):
    def __init__(data):
        # type Dict[str, str]
        self.name = data['Name']
        self.price = data['price']
        self.restaurant = data['Restaurant']
        self.is_breakfast = BREAKFAST in data['Meal Time']
        self.is_lunch = LUNCH in data['Meal Time']
        self.is_dinner = DINNER in data['Meal Time']
        self.calories = data['calories']
        self.fat = data['fat']
        self.carb = data['Carbohydrates']
        self.protein = data['Protein']
        self.vegetarian = data['Vegetarian']
        self.dairy_allergy = data['DairyAllergy']
        self.egg_allergy = data['EggAllergy']
        self.wheat_allergy = data['WheatAllergy']
        self.fish_allergy = data['FishAllergy']
        self.health_choice = data['HealthAllergy']
        self.treenut_allergy = data['TreenutAllergy']
        self.soy_allergy = data['SoyAllergy']
        self.peanut_allergy = data['PeanutAllergy']

    @staticmethod
    def batch_create_by_csv(filename):
        food_entries = read_csv(filename)
        foods = []
        for food in food_entries:
            if 'L/D' in food['Meal Time']:
                # need break up these two.
                try:
                    food['Calories'] = 4.0 * float(food['Protein']) + 4.0* float(food['Carbohydrates']) +9.0*float(food['Fat'])
                except Exception as e:
                    print e
                L_instance = copy(food)
                D_instance = copy(food)
                L_instance['Meal Time'] = 'L'
                D_instance['Meal Time'] = 'D'
                foods.append(L_instance)
                foods.append(D_instance)
            else:
                try:
                    food['Calories'] = 4.0 * float(food['Protein']) + 4.0* float(food['Carbohydrates']) + 9.0*float(food['Fat'])
                except Exception as e:
                    print e
                foods.append(food)   
        return foods