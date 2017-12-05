from scipy.optimize import linprog
from calculator import calculate, calcCalorie
from food import Food
from pulp import *


def identity(n):
    m=[[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        m[i][i] = 1
    return m
    

nutritions = ['Calories', 'Fat', 'Carbohydrates', 'Protein'] 
nut_multiplier = {'Carbohydrates':4, 'Protein':4, 'Fat':9}
nut_lower_percentage = {'Carbohydrates': 0.45, 'Protein': 0.1, 'Fat': 0.2}
nut_higher_percentage = {'Carbohydrates': 0.6, 'Protein': 0.35, 'Fat': 0.35}

def filter_al(foods, allergies):
    def ok(food):
        for nut in nutritions:
            if not food[nut].isdigit():
                return False
        if not food['Price']:
            return False
        return True

    return [food for food in foods if ok(food)]

class Solver(object):

    def __init__(self, height, weight, age, gender, activity, allergy):
        print "in init"
        calorie = calcCalorie(weight, height, gender, age, activity)

        print calorie
        self.nutritions = {
            'Calories':float(calorie),
        }
        self.allergies = allergy

    def run_2(self):
        # GET foods first
        try:
            foods = Food.batch_create_by_csv('data.csv')
            foods = filter_al(foods, [])
        except Exception as e:
            print e

        # Create Problem
        p = LpProblem('p', LpMinimize)

        # Create Variable for each food
        vs = [LpVariable(str(i), 0, cat='Integer') for i, food in enumerate(foods)]

        # set nutrition constraint

        calorie_variable = LpVariable(str('calorie'))
        p += calorie_variable >= self.nutritions['Calories']

        for nut in nutritions:
            if nut != 'Calories':
                coeffs = [float(f[nut]) for f in foods]
                p += nut_multiplier[nut]*lpDot(coeffs, vs) <= calorie_variable * nut_higher_percentage[nut]
                p += nut_multiplier[nut]*lpDot(coeffs, vs) >= calorie_variable * nut_lower_percentage[nut]

        # set B/L/M constraint 
        v_f_pairs = zip(vs, foods)
        breakfasts = [v for v, f in v_f_pairs if f['Meal Time'] =='B']
        lunches = [v for v, f in v_f_pairs if f['Meal Time'] =='L']
        dinners = [v for v, f in v_f_pairs if f['Meal Time'] =='D']
        p += lpSum(breakfasts) == 5
        p += lpSum(lunches) == 5
        p += lpSum(dinners) == 5

        # set diversity constraint 
        same_foods = [[vs[0]]]
        for i in xrange(1, len(v_f_pairs)):
            prev_f = v_f_pairs[i-1][1]
            f = v_f_pairs[i][1]
            if prev_f['Name'] == f['Name']:
                same_foods[-1].append(vs[i])
            else:
                same_foods.append([vs[i]])

        for same_food in same_foods:
            p += lpSum(same_food) <= 2            


        # set objective for minimizing price
        p += lpDot([float(food['Price']) for food in foods],vs)

        self.result = p.solve()
        print self.result
        self.p = p
        self.variables = [v.value() for v in vs]
        
        print self.variables
        self.need_food = []
        for i, v in enumerate(self.variables):
            numbers = int(v)
            food = foods[i]
            for n in xrange(numbers):
                self.need_food.append(food)


        def format_food(food):
            if food['Meal Time'] == 'B':
                food['Time'] = 0
            elif food['Meal Time'] == 'L':
                food['Time'] = 1
            else:
                food['Time'] = 2

        for food in self.need_food:
            try:
                format_food(food)
            except Exception as e:
                print e   

        self.need_money = sum([float(food['Price']) for food in self.need_food])        
        self.total_nutritions = {
            nut: sum([float(food[nut]) for food in self.need_food]) 
            for nut in nutritions
        }
              
        return 

    # def run(self):
    #     # GET foods first
    #     foods = Food.batch_create_by_csv('data.csv')
    #     foods = filter_al(foods, [])

    #     # nutrition 
    #     coeffs = [[-float(food[nut]) for food in foods] for nut in nutritions]

    #     B = [-self.cal, -self.fat, -self.carb, -self.pro]

    #     # meal number constraint 5 meals B/L/D

    #     # Objective, minimize price
    #     C = [food['Price'] for food in foods]

    #     result = linprog(c=C, A_ub = coeffs, b_ub = B)

    #     print result
