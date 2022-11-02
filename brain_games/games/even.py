from random import randint


WELCOME = """Answer "yes" if the number is even, otherwise answer "no"."""
ANSWER_TYPE = str


def game_round():
    ASK_QUESTION = randint(1, 101)
    if ASK_QUESTION % 2 == 0:
        CORRECT_ANSWER = 'yes'
    else:
        CORRECT_ANSWER = 'no'
    return ASK_QUESTION, CORRECT_ANSWER
