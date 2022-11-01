from random import randint

welcome = 'Answer "yes" if given number is prime. Otherwise answer "no".'
answer_type = str


def game_round():
    number = randint(1, 100)
    n = 2
    while number % n != 0:
        n += 1
    if n == number:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    ask_question = number
    return ask_question, correct_answer
