def calculate(weight, height, gender, age):
    '''
    This function compute the calorie(kcal), protein(g), fat(g),
    carbonhydrate(g) needed for a person in one day based on
    his/her weight(kg), height(cm), gender, and age(years).
    '''
    # calorie needed to stay alive
    print "in calculate"
    if gender == "male":
        bmr = 66.5 + (13.7*weight + 5 * height)-(6.76*age)
    else:
        bmr = 66.5+(9.56*weight + 1.8 * height)-(4.68*age)
    # activity level
    # light - 1.37 moderate - 1.55 high = 1.725
    activity_level = 1.55
    calorie = activity_level * bmr
    # protein 0.8-1.2 g per pound
    protein = 0.8 * weight
    # fat
    fat = 0.25 * weight * 2.2
    # carbs
    carb = 0.5 * calorie / 4
    print "ok"
    print (5.0*calorie, 5.0*protein, 5.0*fat, 5.0*carb)
    return (4.0*calorie, 4.0*protein, 4.0*fat, 4.0*carb)

def calculateCalorie(weight, height, gender, age, activity):
    '''
    This algorithm uses Harris–Benedict BMR with activity level factor
    to compute calorie needed per day.
    '''
    if gender=="male":
        BMR = 66.5+(13.75*weight)+(5.003*height)-(6.755*age)
    else:
        BMR = 655.1+(9.563*weight)+(1.850*height)-(4.676*age)
    return activity*BMR
