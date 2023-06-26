from random import randint, choice


RULES = 'What is the result of the expression?'

MIN_NUMBER = 1
MAX_NUMBER = 25

OPERATORS = ('+', '-', '*')


def generate_round():
    """
    """
    operator = choice(OPERATORS)
    number_1 = randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = randint(MIN_NUMBER, MAX_NUMBER)
    question = f"Question: {number_1} {operator} {number_2}"

    match operator:
        case '+':
            correct_answer = str(number_1 + number_2)
        case '-':
            correct_answer = str(number_1 - number_2)
        case '*':
            correct_answer = str(number_1 * number_2)
        case _:
            correct_answer = ''

    return question, correct_answer
