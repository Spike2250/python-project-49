#!/usr/bin/env python3
from random import randint, choice


MIN_NUMBER = 1
MAX_NUMBER = 25

OPERATORS = ('+', '-', '*')


def calc_game():
    """
    """
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

    return question, correct_answer
