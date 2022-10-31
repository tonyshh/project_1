from random import randint
from random import choice


welcome = 'What is the result of the expression?'

def game_round():
    num1 = randint(1 ,101)
    num2 = randint(1, 101)
    math_operation = choice('+-*')
    if math_operation =='+':
        result = num1 + num2
    elif math_operation == '-':
        result = num1 - num2
    elif math_operation == '*':
        result = num1 * num2
    question = f'{num1} {math_operation} {num2}'
    return question,result
