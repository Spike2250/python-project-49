#!/usr/bin/env python3
from brain_games.scripts.game_logic import start_game
from random import randint, choice


# игра "Калькулятор"
def calc_game():
    """
    """
    # правила игры
    rules = 'What is the result of the expression?'
    # создаем список доступных операций
    operators = ('+', '-', '*')
    # создаем пустые списки для вопросов и правильных ответов
    questions = []
    correct_answers = []
    # подготавливаем списки вопросов и правильных ответов
    for i in range(3):
        # случайно выбираем оператор для вопроса
        operator = choice(operators)
        # определяем 2 числа для вопроса в заданном диапазоне
        number1 = randint(1, 25)
        number2 = randint(1, 25)
        # определяем вопрос
        questions.append(f"Question: {number1} {operator} {number2}")
        # определяем правильный ответ
        if operator == '+':
            correct_answers.append(str(number1 + number2))
        elif operator == '-':
            correct_answers.append(str(number1 - number2))
        elif operator == '*':
            correct_answers.append(str(number1 * number2))

    start_game(rules, questions, correct_answers)


# запускаем игру
def main():
    calc_game()


if __name__ == '__main__':
    main()
