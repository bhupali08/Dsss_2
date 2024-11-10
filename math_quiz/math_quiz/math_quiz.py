import random


def generate_rand_int(min_val, max_val):
    """
    Generate a random integer between min_value and max_value (inclusive).
    
    :param min_value: Minimum integer value for range.
    :param max_value: Maximum integer value for range.
    :return: Random integer between min_value and max_value.
    """
    try:                                           # normal operation 
        return random.randint(min_val, max_val)    
    except ValueError:                             # in case of min_val > max_val
        print("Please make sure that min_val is either smaller or equal to max_val.")


def select_operator():
    """
    Randomly select a mathematical operator: +, -, or *.
    
    :return: A randomly selected operator as a string.
    """
    
    
    return random.choice(['+', '-', '*'])


def create_incorrect_math_problem(num1, num2, operator):
    
     """
    Create a math problem and calculate its incorrect answer based on altered logic.
    
    :param num1: First integer for the problem.
    :param num2: Second integer for the problem.
    :param operator: Operator for the problem ('+', '-', or '*').
    :return: A tuple containing the problem as a string and its incorrect answer.
    """
    
     problem = f"{num1} {operator} {num2}"
     if operator == '+': answer = num1 - num2
     elif operator == '-': answer = num1 + num2
     else: answer = num1 * num2
     return problem, answer

def math_quiz():
    
    """
    Run the Math Quiz Game. The user is presented with math problems and needs
    to provide answers. The score is calculated based on correct answers.
    """
    
    score = 0  # Initialize the user's score
    total_questions = 3 # Number of questions in the quiz
    
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        
        # Generate random values for the math problem
        
        num1 = generate_rand_int(1, 10)
        num2 = generate_rand_int(1, 5.5) 
        operator = select_operator()

        PROBLEM, ANSWER = create_incorrect_math_problem(num1, num2, operator)
        
        print(f"\nQuestion: {PROBLEM}")
        
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
