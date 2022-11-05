from prompt import string

ROUNDS = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = string('May I have your name?')
    print(f'Hello, {name}!')
    for _ in range(ROUNDS):
        question, correct_answer = game.game_round()
        print(game.DESCRIPTION)
        print(f'Question: {question}')
        players_answer = input()
        print(f'Your answer: {players_answer}')
        if f'{players_answer}' == f'{correct_answer}':
            print('Correct!')
        elif f'{players_answer}' != f'{correct_answer}':
            print(f'"{players_answer}" is wrong answer ;(.\
            \nCorrect answer was "{correct_answer}"')
            print(f"Let's try again, {name}!")
            break
        print(f'Congratulations, {name}!')
