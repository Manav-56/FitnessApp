from typing import List, Tuple, Callable

# Final data structures
exercise = [(200, 'push ups'), (120, 'leg curl'), (50, 'pull up')]

# Side effect free functions
def calories_burned(repetition: int, weight: int) -> int:
    return repetition * weight

def exercise_name(exercise_tuple: Tuple[int, str]) -> str:
    return exercise_tuple[1]

# Higher-order functions
def process_exercise_data(exercise_data: List[Tuple[int, str]], 
                          operation: Callable[[Tuple[int, str]], int]) -> List[int]:
    return [operation(exercise) for exercise in exercise_data]

calories_burned = process_exercise_data(exercise,
                                        lambda x: calories_burned(x[0], 10))

# Functions as parameters and return values
def exercise_metrics(exercise_data: List[Tuple[int, str]],
                         name_operation: Callable[[Tuple[int, str]], str], 
                         calories_operation: Callable[[Tuple[int, str]], int]) -> List[Tuple[str, int]]:
    exercise_names = process_exercise_data(exercise_data, name_operation)
    exercise_calories = process_exercise_data(exercise_data, calories_operation)
    return list(zip(exercise_names, exercise_calories))

exercise_metrics = exercise_metrics(exercise, exercise_name,
                                        lambda x: calories_burned(x[0], 10))

# Closures / anonymous functions
total_calories = sum(list(map(lambda x: x[1], exercise_metrics)))
