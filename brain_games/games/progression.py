#!/usr/bin/env python3
from brain_games.scripts.brain_games import greeting
from random import randint
from brain_games.game_logic import is_user_answer_correct

ROUNDS = 3

MIN_START_POINT = 0
MAX_START_POINT = 10

MIN_LENGTH = 7
MAX_LENGTH = 10

MIN_STEP = 1
MAX_STEP = 13

MIN_MISSING_INDEX = 1


def progression_game():
    """
    """
    user_name = greeting()
    print('What number is missing in the progression?')
    for i in range(ROUNDS):
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

        if not is_user_answer_correct(user_name, question, correct_answer):
            break
    else:
        print(f"Congratulations, {user_name}!")
