#!/usr/bin/env python3
from random import randint
import math


MIN_NUMBER = 1
MAX_NUMBER = 100


def gcd_game():
    """
    """
    number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = f"Question: {number_1} {number_2}"
    correct_answer = str(math.gcd(number_1, number_2))

    return question, correct_answer
