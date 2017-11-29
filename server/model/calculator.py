def calculate(weight, height, gender, age):
    '''
    This function compute the calorie(kcal), protein(g), fat(g),
    carbonhydrate(g) needed for a person in one day based on
    his/her weight(kg), height(cm), gender, and age(years).
    '''
    # calorie needed to stay alive
    if gender == "male":
        bmr = 66.5 + (13.7*weight + 5 * height)-(6.76*age)
    else:
        bmr = 66.5+(9.56*weight + 1.8 * height)-(4.68*age)
    # activity level
    # light - 1.37 moderate - 1.55 high = 1.725
    activity_level = 1.55
    calorie = activity_level * bmr
    # protein 0.8-1.2 g per pound
    protein = 1.0 * weight * 2.2
    # fat
    fat = 0.25 * weight * 2.2
    # carbs
    carb = (calorie - (protein  * 4 - 9 * fat)) / 4
    return (calorie, protein, fat, carb)
