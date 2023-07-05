import random
def generate_question():
    question_type = random.choice(['algebra', 'geometry', 'trigonometry'])
    if question_type == 'algebra':
        # Generate algebraic question
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        question = f"Solve the equation: {a}x + {b} = {c}"
        solution = (c - b) / a
    elif question_type == 'geometry':
        # Generate geometry question
        shape = random.choice(['rectangle', 'triangle', 'circle'])
        
        if shape == 'rectangle':
            # Calculate the area of a rectangle
            length = random.randint(1, 10)
            breadth = random.randint(1, 10)
            question = f"Find the area of a rectangle with length {length} units and breadth {breadth} units"
            solution = length * breadth
        elif shape == 'triangle':
            base = random.randint(1, 10)
            height = random.randint(1, 10)
            question = f"Find the area of a triangle with base {base} units and height {height} units"
            solution = 0.5 * base * height
        else:
            radius = random.randint(1, 10)
            question = f"Find the circumference of a circle with radius {radius} units (use π = 3.14)"
            solution = 2 * 3.14 * radius
    else:
        angle = random.randint(1, 90)
        question = f"Find the sine of angle {angle} degrees (use π = 3.14)"
        solution = math.sin(math.radians(angle))
    return question, solution
question, solution = generate_question()
print(question)
print("Solution:", solution)

