from brain_games.scripts.brain_games import greeting
import prompt


def start_game(rules: str, questions: list, correct_answers: list):
    """
    Принимает: - правила игры
               - список из 3 вопросов
               - список правильных ответов на них
    Задает вопросы пользователю.
    Если пользователь правильно отвечает на все 3 вопроса - выводит сообщение об успешном прохождении.
    Если дается неверный ответ - выводит сообщение об этом и игра заканчивается.
    """
    # приветствуем пользователя и спрашиваем имя
    user_name = greeting()
    print(rules)
    for i in range(3):
        # выводим вопрос
        print(questions[i])
        # получаем ответ
        answer = prompt.string('Your answer: ')
        # проверяем полученный ответ на правильность
        if answer == correct_answers[i]:
            # выводим сообщение о корректном ответе
            print('Correct!')
        else:
            # выводим сообщение о неверном ответе
            msg = f"'{answer}' is wrong answer ;(. " \
                  f"Correct answer was '{correct_answers[i]}'.\n" \
                  f"Let's try again, {user_name}!"
            print(msg)
            # прерываем цикл
            break
    else:
        # если цикл не прервался - выводим сообщение об успешном прохождении
        print(f"Congratulations, {user_name}!")
