#!/usr/bin/env python3
from brain_games.scripts.brain_games import greeting
from brain_games.game_logic import is_user_answer_correct
from random import randint, choice


ROUNDS = 3

MIN_NUMBER = 1
MAX_NUMBER = 25

OPERATORS = ('+', '-', '*')


def calc_game():
    """
    """
    user_name = greeting()
    print('What is the result of the expression?')
    for i in range(ROUNDS):
        operator = choice(OPERATORS)
        number_1 = randint(MIN_NUMBER, MAX_NUMBER)
        number_2 = randint(MIN_NUMBER, MAX_NUMBER)
        question = f"Question: {number_1} {operator} {number_2}"
        correct_answer = ''
        if operator == '+':
            correct_answer = str(number_1 + number_2)
        elif operator == '-':
            correct_answer = str(number_1 - number_2)
        elif operator == '*':
            correct_answer = str(number_1 * number_2)

        if not is_user_answer_correct(user_name, question, correct_answer):
            break
    else:
        print(f"Congratulations, {user_name}!")
