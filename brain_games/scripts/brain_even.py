#!/usr/bin/env python3
from brain_games.scripts.brain_games import greeting
from random import randint
import prompt


# игра "Проверка на четность"
def even_game():
    '''
    '''

    # приветствуем пользователя и спрашиваем имя
    user_name = greeting()
    # выводим правила игры
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # создаем пустой список для коллекционирования правильных ответов
    correct_answers = []
    # цикл, который завершится после 3 корректных ответов подряд
    while correct_answers != [True, True, True]:
        # задаем новое число для вопроса с помощью randint
        number = randint(1, 100)
        # определяем правильный ответ
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        # выводим вопрос
        print(f"Question: {number}")
        # получаем ответ
        answer = prompt.string('Your answer: ')
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
    even_game()


if __name__ == '__main__':
    main()
