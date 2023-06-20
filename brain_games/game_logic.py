import prompt


def is_user_answer_correct(user_name: str,
                           question: str,
                           correct_answer: str) -> bool:
    """
    задает вопрос пользователю
    сравнивает полученный ответ с правильным
    возвращает True если ответ верен,
               False если ответ с ошибкой
    """
    print(question)
    answer = prompt.string('Your answer: ')
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        msg = f"'{answer}' is wrong answer ;(. " \
              f"Correct answer was '{correct_answer}'.\n" \
              f"Let's try again, {user_name}!"
        print(msg)
        return False
