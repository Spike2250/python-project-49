#!/usr/bin/env python3
from random import randint


MIN_NUMBER = 2
MAX_NUMBER = 199


def prime_number_game():
    """
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = f"Question: {number}"
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer


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
