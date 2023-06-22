import prompt
from brain_games.scripts.brain_games import greeting
from brain_games.games.calc import calc_game
from brain_games.games.even import even_game
from brain_games.games.gcd import gcd_game
from brain_games.games.prime import prime_number_game
from brain_games.games.progression import progression_game


ROUNDS = 3


def start_game(game_type):
    """"""
    match game_type:
        case 'calc':
            rules = 'What is the result of the expression?'
            game = calc_game
        case 'even':
            rules = 'Answer "yes" if the number is even, '\
                    'otherwise answer "no".'
            game = even_game
        case 'gcd':
            rules = 'Find the greatest common divisor of given numbers.'
            game = gcd_game
        case 'prime':
            rules = 'Answer "yes" if given number is prime. '\
                    'Otherwise answer "no".'
            game = prime_number_game
        case 'progression':
            rules = 'What number is missing in the progression?'
            game = progression_game
        case _:
            raise NameError('unidentified game type')

    user_name = greeting()
    print(rules)
    for i in range(ROUNDS):
        question, correct_answer = game()
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
