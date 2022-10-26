#!/usr/bin/env python3
from random import randint
from prompt import string


ROUNDS = 3
counter = 0


print('Welcome to the Brain Games!')
name = string('May I have your name? ')
print('Hello,', name + '!')
print('Answer "yes" if the number is even, otherwise answer "no".')
for _ in range(ROUNDS):
  number = randint(1,100)
  if number%2 == 0:
    correct_answer = 'yes'
  else:
    correct_answer = 'no'
  print(f'Question: {number}')
  players_answer = input()
  print(f'Your answer: {players_answer}')
  if players_answer == correct_answer:
    print('Correct')
    counter+=1
  else:
    print(f'"{players_answer}" is wrong answer ;(. Correct answer was "{correct_answer}"')
    break
  if counter == 3:
    print(f'Congratulations! {name}')

