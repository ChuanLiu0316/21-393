BREAKFAST = 'B'
LUNCH = 'L'
DINNER = 'D'

from reader import read_csv
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
        foods = [Food(data) for data in food_entries]
        return foods