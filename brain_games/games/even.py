#!/usr/bin/env python3
from random import randint


MIN_NUMBER = 1
MAX_NUMBER = 100


def even_game():
    """
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = f"Question: {number}"
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
