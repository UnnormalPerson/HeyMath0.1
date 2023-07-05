import random
import math
def solve_linear_equation(a, b, c):
    if a == 0:
        return None    
    if b == 0:
        if c == 0:
            return 'Any real number'
        else:
            return 'No solution'  
    return (c - b) / a
def calculate_rectangle_area(length, breadth):
    return length * breadth
def calculate_triangle_area(base, height):
    return 0.5 * base * height
def calculate_circle_circumference(radius):
    return 2 * math.pi * radius
def calculate_sine(angle):
    return math.sin(math.radians(angle))
def questiongen(question_number):
    question_type = random.choice(['algebra', 'geometry', 'trigonometry'])
    if question_type == 'algebra':
        lucasxelvin1 = random.randint(1, 10)
        lucasxelvin2 = random.randint(1, 10)
        lucasxelvin3 = random.randint(1, 10)
        question = f"Q{question_number}: Solve the equation: {lucasxelvin1}x + {lucasxelvin2} = {lucasxelvin3}"
        solution = solve_linear_equation(lucasxelvin1, lucasxelvin2, lucasxelvin3)
    elif question_type == 'geometry':
        shape = random.choice(['rectangle', 'triangle', 'circle'])        
        if shape == 'rectangle':
            rheiaxyuwei1 = random.randint(1, 10)
            rheiaxyuwei2 = random.randint(1, 10)
            question = f"Q{question_number}: Find the area of a rectangle with length {rheiaxyuwei1} units and breadth {rheiaxyuwei2} units"
            solution = calculate_rectangle_area(rheiaxyuwei1, rheiaxyuwei2)            
        elif shape == 'triangle':
            rheiaxyuwei1 = random.randint(1, 10)
            rheiaxyuwei2 = random.randint(1, 10)
            question = f"Q{question_number}: Find the area of a triangle with base {rheiaxyuwei1} units and height {rheiaxyuwei2} units"
            solution = calculate_triangle_area(rheiaxyuwei1, rheiaxyuwei2)
        else:
            rheiaxyuwei1 = random.randint(1, 10)
            question = f"Q{question_number}: Find the circumference of a circle with radius {rheiaxyuwei1} units, rounded to the nearest no."
            solution = round(calculate_circle_circumference(rheiaxyuwei1))
    else:
        chengenxamanda1 = random.randint(1, 90)
        question = f"Q{question_number}: Find the sine of angle {chengenxamanda1} degrees"
        solution = calculate_sine(chengenxamanda1)
    return question, solution
def check_answer(question, user_answer, solution):
    if user_answer == solution:
        return True, "Correct!"
    else:
        return False, f"Incorrect. The correct answer is: {solution}"
def main():
    question_number = 1
    score = 0
    total_questions = 0
    while True:
        question, solution = questiongen(question_number)
        print(question)
        user_answer = input("Enter your answer: ")
        try:
            user_answer = float(user_answer)
            is_correct, feedback = check_answer(question, user_answer, solution)
            print(feedback)
            if is_correct:
                score += 1
            total_questions += 1
        except ValueError:
            print("Invalid input. Please enter a number.")
        choice = input("Do you want to continue the quiz? (y/n): ")
        if choice.lower() != 'y':
            break
        question_number += 1
    print("\nQuiz Finished!")
    print("Your score:", score, "/", total_questions)
    percentage_score = (score / total_questions) * 100
    print("Percentage Score:", percentage_score, "%")
if __name__ == "__main__":
    main()
