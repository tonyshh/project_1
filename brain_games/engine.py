from prompt import string


def start(game):

    ROUNDS = 3
    counter = 0

    print('Welcome to the Brain Games!')
    name = string('May I have your name?')
    print(f'Hello, {name}!')
    for _ in range(ROUNDS):
        ASK_QUESTION, CORRECT_ANSWER = game.game_round()
        WELCOME = game.WELCOME
        print(WELCOME)
        print(f'Question {ASK_QUESTION}')
        players_answer = game.answer_type(input())
        print(f'Your answer: {players_answer}')
        if players_answer == CORRECT_ANSWER:
            print('Correct!')
            counter += 1
        else:
            print(f'"{players_answer}" is wrong answer ;(.\
            \nCorrect answer was "{CORRECT_ANSWER}"')
            print(f'Let`s try again {name}')
            break
        if counter == 3:
            print(f'Congratulations! {name}')
