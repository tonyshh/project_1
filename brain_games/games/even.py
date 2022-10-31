from random import randint


welcome = """Answer "yes" if the number is even, otherwise answer "no"."""


def game_round():
    number = randint(1, 101)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
