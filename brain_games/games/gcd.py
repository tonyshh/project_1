import math
from random import randint


welcome = """Find the greatest common divisor of given numbers."""
answer_type = int

def game_round():
    num1 = randint(1, 101)
    num2 = randint(1, 101)
    correct_answer  = math.gcd(num1, num2)
    ask_question = f"{num1} {num2}"


    return correct_answer, ask_question
