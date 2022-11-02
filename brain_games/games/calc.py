from random import randint
from random import choice


WELCOME = 'What is the result of the expression?'
ANSWER_TYPE = int


def game_round():
    num1 = randint(1, 101)
    num2 = randint(1, 101)
    math_operation = choice('+-*')
    if math_operation == '+':
        CORRECT_ANSWER = num1 + num2
    elif math_operation == '-':
        CORRECT_ANSWER = num1 - num2
    elif math_operation == '*':
        CORRECT_ANSWER = num1 * num2
    ask_question = f'{num1} {math_operation} {num2}'
    return ask_question, CORRECT_ANSWER
