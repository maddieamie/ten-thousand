"""Place in root of Ten Thousand Project,
at same level as pyproject.toml
"""

from abc import ABC, abstractmethod
import builtins
import re
from ten_thousand.game import Game
from ten_thousand.game_logic import NewGame


class BaseBot(ABC):
    """
    Base class for Ten Thousand Game bots. Basic code provided by Code Fellows, edited by code author.

    Attributes
    ----------
    last_print : str
        The last printed message.
    last_roll : list
        The last roll of the dice.
    print_all : bool
        Whether to print all messages.
    dice_remaining : int
        The number of dice remaining.
    unbanked_points : int
        The number of unbanked points.
    real_print : function
        The real built-in print function.
    real_input : function
        The real built-in input function.
    total_score : int
        The total score of the bot.
    """

    def __init__(self, print_all=False):
        """
          Initialize a new BaseBot instance.

          Parameters
          ----------
          print_all : bool, optional
              Whether to print all messages (default is False).
          """
        self.last_print = ""
        self.last_roll = []
        self.print_all = print_all
        self.dice_remaining = 0
        self.unbanked_points = 0

        self.real_print = print
        self.real_input = input
        builtins.print = self._mock_print
        builtins.input = self._mock_input
        self.total_score = 0

    def reset(self):
        """
        Restore the real print and input built-in functions.
        """

        builtins.print = self.real_print
        builtins.input = self.real_input

    def report(self, text: str):
        """
        Print out the final score and optionally all other lines.

        Parameters
        ----------
        text : str
            The text to print.
        """

        if self.print_all:
            self.real_print(text)
        elif text.startswith("Thanks for playing."):
            score = re.sub(r"\D", "", text)
            self.total_score += int(score)

    def _mock_print(self, *args, **kwargs):
        """
        Intercept the real built-in print function.

        Parameters
        ----------
        *args : list
            Positional arguments.
        **kwargs : dict
            Keyword arguments.
        """
        str(args)
        line = " ".join(args)
        # uncomment to watch the mock game of the bot
        # self.real_print(f"Mock Print: {line}")

        if "unbanked points" in line:

            # parse the proper string
            # E.g. "You have 700 unbanked points and 2 dice remaining"
            unbanked_points_part, dice_remaining_part = line.split("unbanked points")

            # Hold on to unbanked points and dice remaining for determining rolling vs. banking
            self.unbanked_points = int(re.sub(r"\D", "", unbanked_points_part))

            self.dice_remaining = int(re.sub(r"\D", "", dice_remaining_part))

        elif line.startswith("*** "):
            self.last_roll = [int(die) for die in re.findall(r"\d+", line)]
            # self.last_roll = [int(ch) for ch in line if ch.isdigit()] -> this provided code caused errors
            # print(self.last_roll)

        else:
            self.last_print = line

        self.report(*args, **kwargs)

    def _mock_input(self, *args, **kwargs):
        """
        Intercept the real built-in input function.

        Parameters
        ----------
        *args : list
            Positional arguments.
        **kwargs : dict
            Keyword arguments.

        Returns
        -------
        str
            The simulated input.

        Raises
        -------
        ValueError: If the input does not match the regular game prints, this function will fail.
        """
        # self.real_print(f"Mock Input Prompt: {self.last_print}")

        # added strip func because of errors
        if self.last_print.strip() == '''Welcome to Ten Thousand
(y)es to play or (n)o to decline''':

            return "y"

        elif self.last_print.strip() == '''Enter dice to keep, or (q)uit:''':
            # added additional code line to give state an opportunity to catch up
            stringthing = self._enter_dice()
            return stringthing

        elif self.last_print.strip() == '''(r)oll again, (b)ank your points or (q)uit:''':

            return self._roll_bank_or_quit()

        raise ValueError(f"Unrecognized last print {self.last_print}")

    def _enter_dice(self):
        """
        Simulate user entering which dice to keep.
        Defaults to all scoring dice.

        Returns
        -------
        str
            The string representing dice to keep.
        """
        # static method from NewGame class, inherited from GameLogic
        roll = NewGame.get_scorers(self.last_roll)

        roll_string = "".join(str(value) for value in roll)
        self.report(roll_string)
        print(roll_string)

        return roll_string

    @abstractmethod
    def _roll_bank_or_quit(self):
        """
        Decide whether to roll the dice, bank the points, or quit.
        Subclasses must implement this method.

        Returns
        -------
        str
            The decision ('r', 'b', or 'q').
        """
        pass

    @classmethod
    def play(cls, num_games=10):
        """
        Play the game a given number of times and report the average score.

        Parameters
        ----------
        num_games : int, optional
            The number of games to play (default is 10).
        """

        mega_total = 0

        for _ in range(num_games):
            player = cls()
            game = Game()
            try:
                game.play()
            except SystemExit:
                # a game system exit is fine, that's how the user quits the game
                pass

            mega_total += player.total_score
            player.reset()

        print(
            f"{cls.__name__}: {num_games} games played with average score of {mega_total // num_games}"
        )


class NervousNellie(BaseBot):
    """
    NervousNellie is a bot that always banks the first roll.
    """

    def _roll_bank_or_quit(self) -> str:
        """
         Decide whether to roll the dice, bank the points, or quit.
         NervousNellie always banks the first roll.

         Returns
         -------
         str
             'b' to bank the points.
         """
        return "b"


class BaddieBot(BaseBot):
    """
    BaddieBot is a bot that makes decisions based on the game state.
    The goal is to make sure they have a higher average score than NervousNellie.
    """
    def _roll_bank_or_quit(self) -> str:
        """
        Decide whether to roll the dice, bank the points, or quit.

        Returns
        -------
        str
            The decision ('r', 'b', or 'q').
        """
        if self.dice_remaining == 6 and self.unbanked_points > 0:
            return "r"
        elif 6 > self.dice_remaining >= 3:
            if self.unbanked_points >= 300:
                return "b"
            else:
                return "r"
        else:
            return "b"

    def _enter_dice(self):
        """
        Simulate user entering which dice to keep.
        Defaults to all scoring dice.

        Returns
        -------
        str
            The string representing dice to keep.
        """

        return super()._enter_dice()


if __name__ == "__main__":
    number_games = 100
    NervousNellie.play(number_games)
    BaddieBot.play(number_games)
