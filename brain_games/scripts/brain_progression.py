#!/usr/bin/env python3
from random import randint
from brain_games.scripts.game_logic import start_game


# игра "Какое число пропущенно в арифметической прогрессии"
def progression_game():
    """
    """
    # правила игры
    rules = 'What number is missing in the progression?'
    # создаем пустые списки для вопросов и правильных ответов
    questions = []
    correct_answers = []
    # подготавливаем списки вопросов и правильных ответов
    for i in range(3):
        # случайно задаем критерии прогрессии
        start_point = randint(0, 10)
        length = randint(7, 10)
        step = randint(1, 7)
        # определяем конечную точку для цикла
        end_point = start_point + step * length + 1
        # создаем пустой список для прогрессии
        progression = []
        # создаем прогрессию
        for elem in range(start_point, end_point, step):
            progression.append(str(elem))
        # определяем пропущенный элемент
        index_miss = randint(0, len(progression) - 1)
        # сохраняем правильный ответ
        correct_answers.append(progression[index_miss])
        # меняем значение на ".."
        progression[index_miss] = '..'
        # формируем вопрос
        questions.append(' '.join(progression))

    start_game(rules, questions, correct_answers)


# запускаем игру
def main():
    progression_game()


if __name__ == '__main__':
    main()
