#!/usr/bin/env python3
from brain_games.scripts.brain_games import greeting
from random import randint
import math
from brain_games.game_logic import is_user_answer_correct


ROUNDS = 3

MIN_NUMBER = 1
MAX_NUMBER = 100


def gcd_game():
    """
    """
    user_name = greeting()
    print('Find the greatest common divisor of given numbers.')
    for i in range(ROUNDS):
        number_1 = randint(MIN_NUMBER, MAX_NUMBER)
        number_2 = randint(MIN_NUMBER, MAX_NUMBER)
        question = f"Question: {number_1} {number_2}"
        correct_answer = str(math.gcd(number_1, number_2))

        if not is_user_answer_correct(user_name, question, correct_answer):
            break
    else:
        print(f"Congratulations, {user_name}!")
