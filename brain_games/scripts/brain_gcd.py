#!/usr/bin/env python3
from random import randint
import math
from brain_games.scripts.game_logic import start_game


# игра "Найди наибольший обший делитель"
def gcd_game():
    """
    """
    # правила игры
    rules = 'Find the greatest common divisor of given numbers.'
    # создаем пустые списки для вопросов и правильных ответов
    questions = []
    correct_answers = []
    # подготавливаем списки вопросов и правильных ответов
    for i in range(3):
        # определяем 2 числа для вопроса в заданном диапазоне
        number_1 = randint(1, 100)
        number_2 = randint(1, 100)
        # определяем вопрос
        questions.append(f"Question: {number_1} {number_2}")
        # определяем правильный ответ
        correct_answers.append(str(math.gcd(number_1, number_2)))

    start_game(rules, questions, correct_answers)


# запускаем игру
def main():
    gcd_game()


if __name__ == '__main__':
    main()