'''

In this program, use the following functional programming concepts:

Use final data structures (e.g., lists and tuples) to store the data.
The functions calculate_bmi and bmi_category are side effect free as they only calculate values based on the input parameters and return the result.
The use of higher-order functions is demonstrated by the use of the map and filter functions.
Functions are used as parameters and return values in the average_bmi and bmi_above_average functions.
The bmi_above_average function uses a closure (a function inside another function) to capture the average value for use in the filter function.
'''

from functools import reduce

# side effect free
def calculate_bmi(height, weight):
    return weight / (height ** 2)

# side effect free
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# higher-order functions
def process_bmi(data):
    return list(map(lambda x: (x[0], x[1], calculate_bmi(x[1], x[2]), bmi_category(calculate_bmi(x[1], x[2]))), data))

# Functions are used as parameters and return values
def average_bmi(processed_data):
    return reduce(lambda x, y: x + y[2], processed_data, 0) / len(processed_data)

#  uses a closure (a function inside another function
def bmi_above_average(average, processed_data):
    return list(filter(lambda x: x[2] > average, processed_data))


def main():
    # final data structures
    data = [("John", 1.75, 70), ("Jane", 1.65, 55), ("Jim", 1.90, 85), ("Joan", 1.60, 48)]
    processed_data = process_bmi(data)
    average = average_bmi(processed_data)
    above_average = bmi_above_average(average, processed_data)

    print("Data: ", data)
    print("Processed data: ", processed_data)
    print("Average BMI: ", average)
    print("People with BMI above average: ", above_average)


if __name__ == "__main__":
    main()
