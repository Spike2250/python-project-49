#!/usr/bin/env python3
from random import randint
from brain_games.scripts.game_logic import start_game


def prime_number_game():
    """
    """
    # правила игры
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    # создаем пустые списки для вопросов и правильных ответов
    questions = []
    correct_answers = []
    # подготавливаем списки вопросов и правильных ответов
    for i in range(3):
        # задаем случайное число
        number = randint(2, 199)
        # формируем вопрос
        questions.append(f"Question: {number}")
        # проверяем число на простоту
        if is_prime(number):
            correct_answers.append('yes')
        else:
            correct_answers.append('no')

    start_game(rules, questions, correct_answers)


def is_prime(number: int) -> bool:
    """
    Принимает натуральное число
    Возвращает True, если число простое. False, если нет.

    """
    # проходим циклом по возможным делителям числа number
    # от 2 до number // 2 включительно
    for i in range(2, number // 2 + 1):
        # если число делится на, хотя бы один, делитель
        # без остатка - возвращаем False
        if number % i == 0:
            return False
    # если таких делителей не нашлось - возвращаем True, число простое
    return True


# запускаем игру
def main():
    prime_number_game()


if __name__ == '__main__':
    main()
