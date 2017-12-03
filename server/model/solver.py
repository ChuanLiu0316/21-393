from scipy.optimize import linprog
from calculator import calculate
from food import Food
from pulp import *
def identity(n):
    m=[[0 for x in range(n)] for y in range(n)]
    for i in range(0,n):
        m[i][i] = 1
    return m
    

nutritions = ['Calories', 'Fat', 'Carbohydrates', 'Protein'] 
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

    def __init__(self, height, weight, age, gender):
        print "in init"
        (calorie, protein, fat, carb) = calculate(weight, height, gender, age)
        self.cal = float(calorie)
        self.pro = float(protein)
        self.fat = float(fat)
        self.carb = float(carb)
        print (calorie, protein, fat, carb)

        self.nutritions = {
            'Calories':float(calorie),
            'Fat':float(fat),
            'Carbohydrates': float(carb),
            'Protein': float(protein),
        }

    def run(self):
        # GET foods first
        foods = Food.batch_create_by_csv('data.csv')
        foods = filter_al(foods, [])

        # nutrition 
        coeffs = [[-float(food[nut]) for food in foods] for nut in nutritions]

        B = [-self.cal, -self.fat, -self.carb, -self.pro]

        # meal number constraint 5 meals B/L/D

        # Objective, minimize price
        C = [food['Price'] for food in foods]

        result = linprog(c=C, A_ub = coeffs, b_ub = B)

        print result



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
        for nut in nutritions:
            coeffs = [float(f[nut]) for f in foods]
            p += lpDot(coeffs, vs) >= self.nutritions[nut]

        # set B/L/M constraint 
        v_f_pairs = zip(vs, foods)
        breakfasts = [v for v, f in v_f_pairs if f['Meal Time'] =='B']
        lunches = [v for v, f in v_f_pairs if f['Meal Time'] =='L']
        dinners = [v for v, f in v_f_pairs if f['Meal Time'] =='D']
        p += lpSum(lunches) == 5
        p += lpSum(dinners) == 5
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
        self.p = p
        self.variables = [v.value() for v in vs]

        self.need_food = []
        for i, v in enumerate(self.variables):
            numbers = int(v)
            food = foods[i]
            for n in xrange(numbers):
                self.need_food.append(food)


        self.need_money = sum([float(food['Price']) for food in self.need_food])        
        self.total_nutritions = {
            nut: sum([float(food[nut]) for food in self.need_food]) 
            for nut in nutritions
        }
              
        return 
