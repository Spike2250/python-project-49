from random import randint


RULES = 'What number is missing in the progression?'

MIN_START_POINT = 0
MAX_START_POINT = 10

MIN_LENGTH = 7
MAX_LENGTH = 10

MIN_STEP = 1
MAX_STEP = 13

MIN_MISSING_INDEX = 1


def generate_round():
    """
    """
    start_point = randint(MIN_START_POINT,
                          MAX_START_POINT)
    length = randint(MIN_LENGTH,
                     MAX_LENGTH)
    step = randint(MIN_STEP,
                   MAX_STEP)
    end_point = start_point + step * length + 1

    progression = []
    for elem in range(start_point, end_point, step):
        progression.append(str(elem))

    missing_index = randint(MIN_MISSING_INDEX,
                            len(progression) - 1)
    correct_answer = progression[missing_index]
    progression[missing_index] = '..'
    question = f"Question: {' '.join(progression)}"

    return question, correct_answer
