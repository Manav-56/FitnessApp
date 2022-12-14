print(
        '''
        1 = Calculate Basal metabolic rate
        2 = Major daily calorie needs
        '''
    )
option=int(input('Select any option '))
if option == 1:
    def bmr_computation():
            weight_in_kg = input('Enter Your Weight In Kilogram ')
            if weight_in_kg.isnumeric():
                weight_in_kg=float(weight_in_kg)
            else:
                print('Please Enter a Vaild Input For weight')
                return False

            height_in_cm = input('Enter Your Height In Centimeter ')
            if height_in_cm.isnumeric():
                height_in_cm=int(height_in_cm)
            else:
                print('Please Enter a Vaild Input For height')
                return False

            age = input('Enter Your Age ')
            if age.isnumeric():
                age=int(age)
            else:
                print('Please Enter a Vaild Input For Age')
                return False

            gender = (input('Enter M For Male and F For Female ')).upper()

            if gender == 'M':
                    bmr = int(((10*weight_in_kg)+(6.25*height_in_cm)-(5*age)+5))
                    print('Your Basal metabolic rate is ' + str(bmr) + ' kcal' + '.')

            elif gender == 'F':
                    bmr = int(((10 * weight_in_kg) + (6.25 * height_in_cm) - (5 * age) -161))
                    print('Your Basal metabolic rate(BMR) is ' + str(bmr) + ' kcal' + '.')

            else:
                    print('Please Enter a Vaild Input For Age')

    # BMR = (10 × weight in kg) + (6.25 × height in cm) − (5 × age in years) + 5
    bmr_computation()
elif option == 2:
    def daily_calorie_needs(bmr,weight):
        print(
            '''
            1 = Sedentary: little or no exercise
            2 = Exercise 1-3 times/week
            3 = Exercise 4-5 times/week
            4 = Daily exercise or intense exercise 3-4 times/week	
            5 = Intense exercise 6-7 times/week	
            6 = Very intense exercise daily, or physical job
            '''
        )

        activity_level=int(input('From 1-6 Select your activity level '))
        if activity_level == 1:
            update_bmr=1.2
        elif activity_level == 2:
            update_bmr=1.375
        elif activity_level == 3:
            update_bmr=1.46
        elif activity_level == 4:
            update_bmr=1.55
        elif activity_level == 5:
            update_bmr=1.725
        elif activity_level == 6:
            update_bmr=1.96
        required_cal=int((bmr* update_bmr))
        print('Daily calorie needs for maintaning weight is ' + str(required_cal) +'.')
        print('')

    # calculate macros for maintaining

        #1.5 * your body weight needs to maintain your protein intake
        grams_of_protein = int(1.5*weight)
        # 1 gm of protein = 4 clorie
        calories_protein = int(grams_of_protein*4)

        # 25% of calorie come from fat
        calories_fat = int(.25 * required_cal)
        # 1 gm of fat = 9 clorie
        grams_of_fat = int(calories_fat / 9)

        # 40% of calorie come from carbs
        calories_carbs = int(required_cal-(calories_protein + calories_fat))
        # 1 gm of carbs = 4 clorie
        grams_of_carbs = int(calories_carbs / 4)

        YOU_NEED = 'You need '
        CALORIE = ' calorie and '
        GRAMS_OF_FAT = ' grams of fat.'
        GRAMS_OF_PROTEIN =' grams of protein.'
        GRAMS_OF_CARBS = ' grams of carbs.'

        print('FOR MAINTAING YOUR CALORIES :')
        print(YOU_NEED + str(calories_fat) + CALORIE + str(grams_of_fat) + GRAMS_OF_FAT)
        print(YOU_NEED + str(calories_protein) + CALORIE + str(grams_of_protein) + GRAMS_OF_PROTEIN)
        print(YOU_NEED  + str(calories_carbs) + CALORIE + str(grams_of_carbs) + GRAMS_OF_CARBS)
        print(' ')

    # calculate macros for Bulking
        # for gaining take 200 calorie surplus in BMR
        required_cal+=200
        # 1.75 * your body weight needs to maintain your protein intake
        grams_of_protein = int(1.75 * weight)
        # 1 gm of protein = 4 clorie
        calories_protein = int(grams_of_protein * 4)

        # 25% of calorie come from fat
        calories_fat = int(.25 * required_cal)
        # 1 gm of fat = 9 clorie
        grams_of_fat = int(calories_fat / 9)

        # 40% of calorie come from carbs
        calories_carbs = int(required_cal - (calories_protein + calories_fat))
        # 1 gm of carbs = 4 clorie
        grams_of_carbs = int(calories_carbs / 4)

        print('FOR BULKING YOUR CALORIES :')
        print(YOU_NEED + str(calories_fat) + CALORIE+ str(grams_of_fat) + GRAMS_OF_FAT)
        print(YOU_NEED + str(calories_protein) + CALORIE + str(grams_of_protein) + GRAMS_OF_PROTEIN)
        print(YOU_NEED + str(calories_carbs) + CALORIE + str(grams_of_carbs) + GRAMS_OF_CARBS)
        print(' ')

    # calculate macros for Weight loss
        # for loosing take 200 calorie deficit in BMR
        required_cal = required_cal-200
        # 2.2 * your body weight needs to maintain your protein intake
        grams_of_protein = int(2.2 * weight)
        # 1 gm of protein = 4 clorie
        calories_protein = int(grams_of_protein * 4)

        # 25% of calorie come from fat
        calories_fat = int(.25 * required_cal)
        # 1 gm of fat = 9 clorie
        grams_of_fat = int(calories_fat / 9)

        # 40% of calorie come from carbs
        calories_carbs = int(required_cal - (calories_protein + calories_fat))
        # 1 gm of carbs = 4 clorie
        grams_of_carbs = int(calories_carbs / 4)

        print('FOR LOOSING YOUR CALORIES :')
        print(YOU_NEED + str(calories_fat) + CALORIE + str(grams_of_fat) + GRAMS_OF_FAT)
        print(YOU_NEED + str(calories_protein) + CALORIE + str(grams_of_protein) + GRAMS_OF_PROTEIN)
        print(YOU_NEED + str(calories_carbs) + CALORIE + str(grams_of_carbs) + GRAMS_OF_CARBS)

    bmr = int(input('Enter Your Basal metabolic rate(BMR) in kcal '))
    weight=int(input('Enter Your weight in kilograms '))
    daily_calorie_needs(bmr,weight)


