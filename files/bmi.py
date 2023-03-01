from pywebio.input import input, FLOAT
from pywebio.output import put_text
from py_edamam import Edamam
from copy import deepcopy

PUT_TEXT = put_text
INPUT = input


class MetabolicRate:
    def __init__(self, weight_in_kg, height_in_cm, age, gender):
        self.weight_in_kg = weight_in_kg
        self.height_in_cm = height_in_cm
        self.age = age
        self.gender = gender.upper()

    def bmr_cal(self):
        if self.gender == "M":
            bmr = int(
                (
                    (10 * self.weight_in_kg)
                    + (6.25 * self.height_in_cm)
                    - (5 * self.age)
                    + 5
                )
            )

        elif self.gender == "F":
            bmr = int(
                (
                    (10 * self.weight_in_kg)
                    + (6.25 * self.height_in_cm)
                    - (5 * self.age)
                    - 161
                )
            )

        PUT_TEXT("Your Basal metabolic rate is " + str(bmr) + " kcal" + ".")


class BodyMassIndex:
    def __init__(self, bmi):
        self.bmi = bmi

    def bmi_index(self):
        if self.bmi <= 18.5:
            PUT_TEXT("You are underweight.")
        elif self.bmi <= 24.9:
            PUT_TEXT("You are normal weight.")
        elif self.bmi <= 29.9:
            PUT_TEXT("You are overweight.")
        else:
            PUT_TEXT("You are obese.")


class DailyCalorieNeeds:
    YOU_NEED = "You need "
    CALORIE = " calorie and "
    GRAMS_OF_FAT = " grams of fat."
    GRAMS_OF_PROTEIN = " grams of protein."
    GRAMS_OF_CARBS = " grams of carbs."

    def __init__(self, bmr, weight):
        self.bmr = bmr
        self.weight = weight
        self.required_cal = 0

    @staticmethod
    def calculate_macros(weight, protein_scale, required_cal, text):
        # 1.75 * your body weight needs to maintain your protein intake
        grams_of_protein = int(protein_scale * weight)
        # 1 gm of protein = 4 clorie
        calories_protein = int(grams_of_protein * 4)

        # 25% of calorie come from fat
        calories_fat = int(0.25 * required_cal)
        # 1 gm of fat = 9 clorie
        grams_of_fat = int(calories_fat / 9)

        # 40% of calorie come from carbs
        calories_carbs = int(required_cal - (calories_protein + calories_fat))
        # 1 gm of carbs = 4 clorie
        grams_of_carbs = int(calories_carbs / 4)

        PUT_TEXT(text)
        PUT_TEXT(
            DailyCalorieNeeds.YOU_NEED
            + str(calories_fat)
            + DailyCalorieNeeds.CALORIE
            + str(grams_of_fat)
            + DailyCalorieNeeds.GRAMS_OF_FAT
        )
        PUT_TEXT(
            DailyCalorieNeeds.YOU_NEED
            + str(calories_protein)
            + DailyCalorieNeeds.CALORIE
            + str(grams_of_protein)
            + DailyCalorieNeeds.GRAMS_OF_PROTEIN
        )
        PUT_TEXT(
            DailyCalorieNeeds.YOU_NEED
            + str(calories_carbs)
            + DailyCalorieNeeds.CALORIE
            + str(grams_of_carbs)
            + DailyCalorieNeeds.GRAMS_OF_CARBS
        )
        PUT_TEXT(" ")

    def calculate_macros_for_maintaining(self):
        required_cal = deepcopy(self.required_cal)

        DailyCalorieNeeds.calculate_macros(
            self.weight, 1.5, required_cal, "FOR MAINTAING YOUR CALORIES :"
        )

    def calculate_macros_for_bulking(self):
        required_cal = deepcopy(self.required_cal)

        # for gaining take 200 calorie surplus in BMR
        required_cal += 200

        DailyCalorieNeeds.calculate_macros(
            self.weight, 1.75, required_cal, "FOR BULKING YOUR CALORIES :"
        )

    def calculate_macros_for_weight_loss(self):
        required_cal = deepcopy(self.required_cal)

        DailyCalorieNeeds.calculate_macros(
            self.weight, 2.2, required_cal, "FOR LOOSING YOUR CALORIES :"
        )

    def daily_calorie_needs(self):
        PUT_TEXT(
            """
            1 = Sedentary: little or no exercise
            2 = Exercise 1-3 times/week
            3 = Exercise 4-5 times/week
            4 = Daily exercise or intense exercise 3-4 times/week	
            5 = Intense exercise 6-7 times/week	
            6 = Very intense exercise daily, or physical job
        """
        )

        update_bmr = 0
        activity_level = int(INPUT("From 1-6 Select your activity level "))

        if activity_level == 1:
            update_bmr = 1.2
        elif activity_level == 2:
            update_bmr = 1.375
        elif activity_level == 3:
            update_bmr = 1.46
        elif activity_level == 4:
            update_bmr = 1.55
        elif activity_level == 5:
            update_bmr = 1.725
        elif activity_level == 6:
            update_bmr = 1.96
        self.required_cal = int((self.bmr * update_bmr))

        PUT_TEXT(
            "Daily calorie needs for maintaning weight is "
            + str(self.required_cal)
            + "."
        )
        PUT_TEXT("")

        self.calculate_macros_for_bulking()
        self.calculate_macros_for_maintaining()
        self.calculate_macros_for_weight_loss()


class CalFatProtienSugarForFood:
    def __init__(self, food="1 apple"):
        self.food = food
        self.e = Edamam(
            
            # here you have to add your credentials 
            nutrition_appid="",
            nutrition_appkey="",
        )

    def search_nutrient(self):
        result = self.e.search_nutrient(self.food)
        PUT_TEXT("CALORIES: " + str(result["calories"]) + " cal")
        PUT_TEXT("FAT: " + str(result["totalNutrients"]["FAT"]["quantity"]) + " g")
        PUT_TEXT("SUGAR: " + str(result["totalNutrients"]["SUGAR"]["quantity"]) + " g")
        PUT_TEXT(
            "PROTEIN: " + str(result["totalNutrients"]["PROCNT"]["quantity"]) + " g"
        )


if __name__ == "__main__":
    from pywebio.output import use_scope
    from pywebio.input import actions

    put_text(
        """
        1 = Calculate Basal metabolic rate
        2 = Calculate Body Mass Index 
        3 = Major daily calorie needs
        4 = Get Cal,Fat,Protein and Sugar for your food
    """
    )
    while True:
        option = input("Select any option ", type=FLOAT)
        with use_scope("result", clear=True):
            if option == 1:
                weight_in_kg = input("Enter Your Weight In Kilogram ", type=FLOAT)
                height_in_cm = input("Enter Your Height In Centimeter ", type=FLOAT)
                age = input("Enter Your Age ", type=FLOAT)
                gender = (input("Enter M For Male and F For Female ")).upper()
                mrate = MetabolicRate(weight_in_kg, height_in_cm, age, gender)
                mrate.bmr_cal()

            if option == 2:
                bmi = input("Enter your BMI: ", type=FLOAT)
                bmi_obj = BodyMassIndex(bmi)
                bmi_obj.bmi_index()

            if option == 3:
                bmr = input("Enter Your Basal metabolic rate(BMR) in kcal ", type=FLOAT)
                weight = input("Enter Your weight in kilograms ", type=FLOAT)
                calory_needs = DailyCalorieNeeds(bmr, weight)
                calory_needs.daily_calorie_needs()

            if option == 4:
                put_text(
                    "The format must be `number food`. For example, 1 apple, 2 egg, or 3 apple"
                )
                food = input("Enter food: ")
                cfpsforfood = CalFatProtienSugarForFood(food)
                cfpsforfood.search_nutrient()

        if actions("Continue?", ["continue", "exit"]) == "exit":
            break
