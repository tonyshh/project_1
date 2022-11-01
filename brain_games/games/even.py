from random import randint


welcome = """Answer "yes" if the number is even, otherwise answer "no"."""
answer_type = str


def game_round():
    ask_question = randint(1, 101)
    if ask_question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return ask_question, correct_answer
