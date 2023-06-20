#!/usr/bin/env python3
from brain_games.scripts.brain_games import greeting
from random import randint
from brain_games.game_logic import is_user_answer_correct


ROUNDS = 3

MIN_NUMBER = 2
MAX_NUMBER = 199


def prime_number_game():
    """
    """
    user_name = greeting()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for i in range(ROUNDS):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        question = f"Question: {number}"
        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if not is_user_answer_correct(user_name, question, correct_answer):
            break
    else:
        print(f"Congratulations, {user_name}!")


def is_prime(number: int) -> bool:
    """
    """
    if number > 1:
        for i in range(2, number // 2 + 1):
            if number % i == 0:
                return False
        return True
    else:
        return False
