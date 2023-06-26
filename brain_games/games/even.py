from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'

MIN_NUMBER = 1
MAX_NUMBER = 100


def generate_round():
    """
    """
    number = randint(MIN_NUMBER, MAX_NUMBER)
    question = f"Question: {number}"
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer
