from random import randint
import math


RULES = 'Find the greatest common divisor of given numbers.'

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round():
    """
    """
    number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = f"Question: {number_1} {number_2}"
    correct_answer = str(math.gcd(number_1, number_2))

    return question, correct_answer
