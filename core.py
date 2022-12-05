def bmr_computation():
    while True:
        weight_in_kg = input('Enter Your Weight In Kilogram ')
        if weight_in_kg.isnumeric():
            weight_in_kg=float(weight_in_kg)
        else:
            print('Please Enter a Vaild Input For weight')
            break

        height_in_cm = input('Enter Your Height In Centimeter ')
        if height_in_cm.isnumeric():
            height_in_cm=int(height_in_cm)
        else:
            print('Please Enter a Vaild Input For height')
            break


        age = input('Enter Your Age ')
        if age.isnumeric():
            age=int(age)
        else:
            print('Please Enter a Vaild Input For Age')
            break

        gender = (input('Enter M For Male and F For Female ')).upper()

        if gender == 'M':
                bmr = int(((10*weight_in_kg)+(6.25*height_in_cm)-(5*age)+5))
                print('Your Basal metabolic rate is ' + str(bmr) + ' kcal' + '.')
                break
        elif gender == 'F':
                bmr = int(((10 * weight_in_kg) + (6.25 * height_in_cm) - (5 * age) -161))
                print('Your Basal metabolic rate(BMR) is ' + str(bmr) + ' kcal' + '.')
                break
        else:
                print('Please Enter a Vaild Input For Age')
                break




# BMR = (10 × weight in kg) + (6.25 × height in cm) − (5 × age in years) + 5
bmr_computation()

