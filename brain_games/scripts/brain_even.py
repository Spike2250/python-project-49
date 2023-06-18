#!/usr/bin/env python3
from brain_games.scripts.game_logic import start_game
from random import randint


# игра "Проверка на четность"
def even_game():
    """
    """
    # выводим правила игры
    rules = 'Answer "yes" if the number is even, otherwise answer "no".'
    # создаем пустые списки для вопросов и правильных ответов
    questions = []
    correct_answers = []
    # цикл, который завершится после 3 корректных ответов подряд
    for i in range(3):
        # задаем новое число для вопроса в заданном диапазоне
        number = randint(1, 100)
        # определяем правильный ответ
        if number % 2 == 0:
            correct_answers.append('yes')
        else:
            correct_answers.append('no')
        # выводим вопрос
        questions.append(f"Question: {number}")

    start_game(rules, questions, correct_answers)


# запускаем игру
def main():
    even_game()


if __name__ == '__main__':
    main()
