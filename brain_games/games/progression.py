from random import randint

welcome = 'What number is missing in the progression?'
answer_type = int


def game_round():
    num1 = randint(1, 10)
    num2 = randint(80, 100)
    n = randint(2, 10)
    progression = []
    progression = list(range(num1, num2, n))
    index = randint(1, len(progression) - 1)
    correct_answer = progression[index]
    progression[index] = '..'
    rebuild_progression = (' '.join(map(str, progression)))
    ask_question = rebuild_progression

    return ask_question, correct_answer
