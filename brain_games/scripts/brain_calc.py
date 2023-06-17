#!/usr/bin/env python3
from brain_games.scripts.brain_games import greeting
from random import randint, choice
import prompt      


# игра "Калькулятор"
def calc_game():
    """
    """
    # приветствуем пользователя и спрашиваем имя
    user_name = greeting()
    # выводим правила игры
    print('What is the result of the expression?')
    # создаем пустой список для коллекционирования правильных ответов
    correct_answers = []
    # 
    operators = ('+', '-', '*')
    # цикл, который завершится после 3 корректных ответов подряд
    while correct_answers != [True, True, True]:
        # случайно выбираем оператор для вопроса
        operator = choice(operators)
        # определяем 2 числа для вопроса
        number1 = randint(1, 25)
        number2 = randint(1, 25)
        # определяем вопрос
        question = f"Question: {number1} {operator} {number2}"
        #
        correct_answer = 0
        # определяем правильный ответ
        if operator == '+':
            correct_answer = number1 + number2
        elif operator == '-':
            correct_answer = number1 - number2
        elif operator == '*':
            correct_answer = number1 * number2
        # выводим вопрос
        print(question)
        # получаем ответ
        answer = int(prompt.string('Your answer: '))
        # проверяем полученный ответ на правильность
        if answer == correct_answer:
            # выводим сообщение о корректном ответе
            print('Correct!')
            correct_answers.append(True)
        else:
            # выводим сообщение о неверном ответе
            msg = f"'{answer}' is wrong answer ;(. "\
                  f"Correct answer was '{correct_answer}'.\n"\
                  f"Let's try again, {user_name}!"
            print(msg)
            # прерываем цикл
            break
    else:
        # если цикл не прервался - выводим сообщение об успешном прохождении
        print(f"Congratulations, {user_name}!")


# запускаем игру
def main():
    calc_game()


if __name__ == '__main__':
    main()
