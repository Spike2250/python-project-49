import prompt
from brain_games.scripts.brain_games import greeting


ROUNDS = 3


def start_game(game):
    """"""
    user_name = greeting()
    print(game.RULES)
    for i in range(ROUNDS):
        question, correct_answer = game.generate_round()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            msg = f"'{answer}' is wrong answer ;(. " \
                  f"Correct answer was '{correct_answer}'.\n" \
                  f"Let's try again, {user_name}!"
            print(msg)
            break
    else:
        print(f"Congratulations, {user_name}!")
