from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_round():
    number = randint(1, 100)
    n = 2
    while number % n != 0:
        n += 1
    if n == number:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = number
    return question, correct_answer
