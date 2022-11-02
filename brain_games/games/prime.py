from random import randint

WELCOME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
ANSWER_TYPE = str


def game_round():
    number = randint(1, 100)
    n = 2
    while number % n != 0:
        n += 1
    if n == number:
        CORRECT_ANSWER = 'yes'
    else:
        CORRECT_ANSWER = 'no'

    ASK_QUESTION = number
    return ASK_QUESTION, CORRECT_ANSWER
