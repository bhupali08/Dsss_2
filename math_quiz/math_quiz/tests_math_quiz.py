import unittest
from math_quiz import generate_rand_int, select_operator, create_incorrect_math_problem


class TestMathGame(unittest.TestCase):

    def test_generate_rand_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = generate_rand_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_select_operator(self):
        valid_operators =  ['+', '-', '*']
        generated_operator = select_operator()
        self.assertIn(generated_operator, valid_operators) #check if gererated_operator is within valid_operators
        
        

    def test_create_incorrect_math_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (100, 4, '-', '100 - 4', 96),  
                (10, 2, '*', '10 * 2', 12),   
                (80, 20, '+', '80 + 20', 100),   
                (6, 2, '-', '6 - 2', 4),   
                (1, 7, '*', '1 * 7', 7),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                generated_problem, generated_answer = create_incorrect_math_problem(num1, num2, operator)
                
                self.assertEqual(generated_problem, expected_problem)
                self.assertEqual(generated_answer, expected_answer) 

if __name__ == "__main__":
    unittest.main()
