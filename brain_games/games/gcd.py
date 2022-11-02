import math
from random import randint


WELCOME = """Find the greatest common divisor of given numbers."""
ANSWER_TYPE = int


def game_round():
    num1 = randint(1, 101)
    num2 = randint(1, 101)
    CORRECT_ANSWER = math.gcd(num1, num2)
    ASK_QUESTION = f"{num1} {num2}"

    return ASK_QUESTION, CORRECT_ANSWER
