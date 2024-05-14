from ten_thousand.game_logic import NewGame
from ten_thousand.mock_roller import MockRoller

import sys


def first_welcome(sim=False, sim_number=0):

    print('''Welcome to Ten Thousand
(y)es to play or (n)o to decline''')
    welcome_input = input('> ')
    welcome_input = welcome_input.lower().strip()

    if welcome_input == 'n':
        print('OK. Maybe another time')
        sys.exit()
    elif welcome_input == 'y':
        new_game_instance = NewGame()
        if sim is True and sim_number != 0:
            new_mock = MockRoller()
            play(new_mock.mock_roller, new_game_instance, sim_number)
        else:
            play(new_game_instance.roll_dice, new_game_instance, sim_number)
    else:
        print('Sorry, I did not understand your command. Please enter y for yes, n for no.')


def quit_program(score_player_1):
    print(f'Thanks for playing. You earned {score_player_1} points')
    sys.exit()


def play(roller, new_game, sim_number):

    while True:
        new_game.change_round()
        if sim_number != 0:
            new_game.keep_track_of_dice_roll(roller(sim_number))
        else:
            new_game.keep_track_of_dice_roll(roller(6))

        # print('Current Roll:', new_game.dice_roll, new_game.dice_just_rolled)
        while new_game.dice_left_to_roll > 0:
            # print(new_game.dice_roll)
            new_game.check_for_farkle()
            if new_game.dice_left_to_roll == 0:
                break
            else:
                print('Enter dice to keep, or (q)uit:')

                player_input = input('> ')
                if player_input == 'q':
                    quit_program(new_game.score_player_1)
                else:
                    filtered = new_game.keep_new_input(player_input)
                    # print(filtered)
                    input_result = new_game.keep_dice(filtered)
                    # print('Dice to calculate score:', new_game.dice_to_calculate_score)
                    if input_result is True:
                        continue
                    else:

                        print('(r)oll again, (b)ank your points or (q)uit:')

                        player_input_2 = input('> ')
                        if player_input_2 == 'r':
                            if sim_number != 0:
                                new_game.keep_track_of_dice_roll(roller(sim_number))
                            else:
                                new_game.keep_track_of_dice_roll(roller(new_game.dice_left_to_roll))

                        elif player_input_2 == 'b':
                            new_game.update_score()
                            break
                        elif player_input_2 == 'q':
                            quit_program(new_game.score_player_1)
                        else:
                            print('Sorry, invalid input. Please try again.')
                            continue


if __name__ == '__main__':
    first_welcome()


