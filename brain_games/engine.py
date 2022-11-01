from prompt import string


def start(game):

    ROUNDS = 3
    counter = 0

    print('Welcome to the Brain Games!')
    name = string('May I have your name?')
    print(f'Hello, {name}!')
    for _ in range(ROUNDS):
        ask_question, correct_answer = game.game_round()
        welcome = game.welcome
        print(welcome)
        print(f'Question {ask_question}')
        players_answer = game.answer_type(input())
        print(f'Your answer: {players_answer}')
        if players_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f'"{players_answer}" is wrong answer ;(.\
            \nCorrect answer was "{correct_answer}"')
            print(f'Let`s try again {name}')
            break
        if counter == 3:
            print(f'Congratulations! {name}')
