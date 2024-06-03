from ten_thousand.game_logic import NewGame
from ten_thousand.mock_roller import MockRoller

import sys


class Game:
    """
      Class to manage the Ten Thousand game state.

      Attributes
      ----------
      new_game : NewGame or None
          The current game instance or None if no game is active.
    """
    def __init__(self):
        """
        Initialize a new Game instance.
        """
        self.new_game: NewGame | None = None

    def play(self, sim: bool = False, sim_number: int = 0) -> None:
        """
        Start the game and handle user input for starting or declining the game.

        Parameters
        ----------
        sim : bool, optional
            If True, the game will use a mock roller for simulation, by default False.
        sim_number : int, optional
            If sim = True, input a number for the simulation from the MockRoller class, by default 0.

        Returns
        -------
        None
        """

        print('''Welcome to Ten Thousand
(y)es to play or (n)o to decline''')
        welcome_input = input('> ')
        welcome_input = welcome_input.lower().strip()

        if welcome_input == 'n':
            print('OK. Maybe another time')
            sys.exit()
        elif welcome_input == 'y':
            self.new_game = NewGame()
            if sim is True and sim_number != 0:
                # creates an instance of MockRoller & uses sim number chosen when calling the method
                new_mock = MockRoller()
                self.start_game(new_mock.mock_roller, sim_number)
            else:
                # starts the game with the default roller in the NewGame class
                self.start_game(self.new_game.roll_dice, sim_number)
        else:
            print('Sorry, I did not understand your command. Please enter y for yes, n for no.')

    def quit_program(self) -> None:
        """
        Quit the program and print the final score.

        Returns
        -------
        None
        """
        print(f'Thanks for playing. You earned {self.new_game.score_player_1} points')
        sys.exit()

    def start_game(self, roller: callable, sim_number: int) -> None:
        """
        Start the game rounds, handle dice rolling, and user interactions.

        Parameters
        ----------
        roller : callable
            Function to roll the dice. This should be a static method.
        sim_number : int
            The int is the simulation number for the MockRoller class, or 0 if no sim is happening.

        Returns
        -------
        None
        """

        while True:
            # when the number of game rounds hits 20, exit the game
            if self.new_game.round == 20:
                self.quit_program()
            # resets the round each time the loop runs
            self.new_game.change_round()
            # Keeps track of the dice rolled by the game to prevent cheating
            if sim_number != 0:
                self.new_game.keep_track_of_dice_roll(roller(sim_number))
            else:
                self.new_game.keep_track_of_dice_roll(roller(6))

            # To see state: print('Current Roll:', self.new_game.dice_roll, self.new_game.dice_just_rolled)
            while self.new_game.dice_left_to_roll > 0:
                # this line with get_scorers is optional
                self.new_game.get_scorers(self.new_game.dice_roll)
                # checks to see if there are any scoring dice, if not, it resets the round
                self.new_game.check_for_farkle()
                if self.new_game.dice_left_to_roll == 0:
                    break
                else:
                    print('Enter dice to keep, or (q)uit:')

                    player_input = input('> ')
                    if player_input == 'q':
                        self.quit_program()
                    else:
                        # filters out everything but the ints provided
                        filtered = self.new_game.keep_new_input(player_input)
                        # checks user input with system dice roll to see if the roll is possible or not
                        input_result = self.new_game.keep_dice(filtered)
                        # if the user inputs an impossible dice roll, it will restart this mini loop
                        if input_result is True:
                            continue
                        else:

                            print('(r)oll again, (b)ank your points or (q)uit:')

                            player_input_2 = input('> ')
                            if player_input_2 == 'r':
                                # roll the simulation number, otherwise roll remaining dice
                                if sim_number != 0:
                                    self.new_game.keep_track_of_dice_roll(roller(sim_number))
                                else:
                                    self.new_game.keep_track_of_dice_roll(roller(self.new_game.dice_left_to_roll))

                            elif player_input_2 == 'b':
                                # updates the player's score total & breaks loop
                                self.new_game.update_score()
                                break
                            elif player_input_2 == 'q':
                                self.quit_program()
                            else:
                                # just here in case something goes wrong
                                print('Sorry, invalid input. Please try again.')
                                continue


if __name__ == '__main__':
    game = Game()
    game.play()


