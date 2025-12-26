import random

# ------------------------------
# Configuration constants
# ------------------------------
MIN = 0
MAX = 9
OPERATORS = ["+", "-", "*", "/"]
NUMBER_OF_QN = 10


# Ask a fixed number of arithmetic questions
for _ in range(NUMBER_OF_QN):

    # --------------------------------
    # Generate operands and operator
    # --------------------------------
    left = random.randint(MIN, MAX)
    operator = random.choice(OPERATORS)

    # Prevent division by zero
    if operator == "/":
        right = random.randint(1, MAX)
    else:
        right = random.randint(MIN, MAX)

    # --------------------------------
    # Compute the correct answer
    # --------------------------------
    if operator == "+":
        correctAnswer = left + right
    elif operator == "-":
        correctAnswer = left - right
    elif operator == "*":
        correctAnswer = left * right
    else:
        # Division produces a float; limit precision
        correctAnswer = round(left / right, 3)

    # --------------------------------
    # Prompt the user until correct
    # --------------------------------
    while True:
        try:
            if operator == "/":
                # Accept decimal answers for division
                userAnswer = round(
                    float(input(
                        f"{left} / {right} = (round to 3 decimal places) "
                    )),
                    3
                )
            else:
                # Enforce integer answers for other operators
                userAnswer = int(input(f"{left} {operator} {right} = "))

        except ValueError:
            # Handle non-numeric input gracefully
            print("Please enter a valid number.")
            continue

        # Check the user's answer
        if userAnswer == correctAnswer:
            print("Correct!\n")
            break
        else:
            print("Incorrect. Try again.")
