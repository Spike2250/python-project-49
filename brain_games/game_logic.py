import prompt
from brain_games.scripts.brain_games import greeting
from brain_games.games import calc, even, gcd, prime, progression


ROUNDS = 3


def define_rules_and_mechanics(game_type):
    """"""
    games = {
        'calc': calc,
        'even': even,
        'gcd': gcd,
        'prime': prime,
        'progression': progression
    }
    if game_type in games:
        rules = games[game_type].RULES
        generate_round = games[game_type].generate_round
    else:
        raise NameError('unidentified game type')

    return rules, generate_round


def start_game(game_type):
    """"""
    rules, generate_question_answer = define_rules_and_mechanics(game_type)

    user_name = greeting()
    print(rules)
    for i in range(ROUNDS):
        question, correct_answer = generate_question_answer()
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
