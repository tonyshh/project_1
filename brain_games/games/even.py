from random import randint


DESCRIPTION = """Answer "yes" if the number is even, otherwise answer "no"."""


def game_round():
    question = randint(1, 101)
    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer
