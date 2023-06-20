#!/usr/bin/env python3
from brain_games.scripts.brain_games import greeting
from brain_games.game_logic import is_user_answer_correct
from random import randint


ROUNDS = 3

MIN_NUMBER = 1
MAX_NUMBER = 100


def even_game():
    """
    """
    user_name = greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(ROUNDS):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        question = f"Question: {number}"
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if not is_user_answer_correct(user_name, question, correct_answer):
            break
    else:
        print(f"Congratulations, {user_name}!")
