from ten_thousand.game_logic import GameLogic
from ten_thousand.mock_roller import play_dice
import sys


def first_welcome(roller=GameLogic.roll_dice):
    print('''Welcome to Ten Thousand
(y)es to play or (n)o to decline''')
    welcome_input = input('> ')
    welcome_input = welcome_input.lower().strip()

    if welcome_input == 'n':
        print('OK. Maybe another time')
        sys.exit()
    elif welcome_input == 'y':
        play()
    else:
        print('Sorry, I did not understand your command. Please enter y for yes, n for no.')


def quit_program(score_player_1):
    print(f'Thanks for playing. You earned {score_player_1} points')
    sys.exit()


def play(roller=GameLogic.roll_dice):
    new_game = GameLogic()

    while True:
        new_game.change_round()
        new_game.roll_dice(6)
        while new_game.dice_left_to_roll > 0:
            print('Enter dice to keep, or (q)uit:')

            player_input = input('> ')
            if player_input == 'q':
                quit_program(new_game.score_player_1)
            else:
                new_game.keep_dice(player_input)

            print('(r)oll again, (b)ank your points or (q)uit:')

            player_input_2 = input('> ')
            if player_input_2 == 'r':
                new_game.roll_dice(new_game.dice_left_to_roll)
            elif player_input_2 == 'b':
                new_game.update_score()
                break
            elif player_input_2 == 'q':
                quit_program(new_game.score_player_1)


if __name__ == '__main__':
    first_welcome()
    play()

