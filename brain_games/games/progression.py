from random import randint

WELCOME = 'What number is missing in the progression?'
ANSWER_TYPE = int


def game_round():
    num1 = randint(1, 10)
    num2 = randint(80, 100)
    n = randint(2, 10)
    progression = []
    progression = list(range(num1, num2, n))
    index = randint(1, len(progression) - 1)
    CORRECT_ANSWER = progression[index]
    progression[index] = '..'
    rebuild_progression = (' '.join(map(str, progression)))
    ASK_QUESTION = rebuild_progression

    return ASK_QUESTION, CORRECT_ANSWER
