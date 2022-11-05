import math
from random import randint


DESCRIPTION = """Find the greatest common divisor of given numbers."""


def game_round():
    num1 = randint(1, 101)
    num2 = randint(1, 101)
    correct_answer = math.gcd(num1, num2)
    question = f"{num1} {num2}"

    return question, correct_answer
