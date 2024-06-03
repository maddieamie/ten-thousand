import random
import ast


class GameLogic:
    """
    A class to handle the game logic for Ten Thousand.

    Attributes
    ----------
    dice_left_to_roll : int
        Number of dice left to roll in the round.
    dice_just_rolled : dict
        A dictionary to keep track of the count of each dice value just rolled.
    dice_roll : tuple
        A tuple to store the current dice roll as a tuple.
    dice_to_calculate_score : dict
        A dictionary to keep track of dice values that the user entered in order to calculate their points.
    unbanked_points : int
        Points that have been scored but not yet banked.
    turn : range
        A range representing the current turn. Not in use for this version, could be for the future.
    score_player_1 : int
        Score of player 1, which is the only player in this version.
    score_computer : int
        Score of the computer. Not in use for this version, could be for the future.
    round : int
        Current round number of the game state.
    """
    def __init__(self):
        """
        Initialize a new GameLogic instance.
        """
        self.dice_left_to_roll = 6
        self.dice_just_rolled = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }
        self.dice_roll = ()
        self.dice_to_calculate_score = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }
        self.unbanked_points = 0
        self.turn = range(0, 1 + 1)
        self.score_player_1 = 0
        self.score_computer = 0
        self.round = 0

    @staticmethod
    def calculate_score(dice_roll_tuple: tuple) -> int:
        """
        Calculate the score for a given dice roll.

        Parameters
        ----------
        dice_roll_tuple : tuple
            A tuple representing the dice roll.

        Returns
        -------
        int
            The calculated score.
        Raises
        -------
        ValueError: Amount of dice exceeding six
        ValueError: If value of dice number exceeds six
        """

        score = 0
        three_pairs = False
        straight = False

        # checks to see if dice entered is possible
        if len(dice_roll_tuple) > 6:
            raise ValueError("Invalid dice value encountered")

        # keeps track of things in this method only
        score_dictionary: dict[int, int] = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }

        # Iterate through the input tuple and update counts in dict
        for num in dice_roll_tuple:
            if num in score_dictionary:
                score_dictionary[num] += 1
            else:
                raise ValueError("Invalid dice value encountered")

            # checks to see if there is one of each value, if so enters this score & changes boolean to true
            if all(score_dictionary[num] == 1 for num in range(1, 7)):
                score += 1500  # Straight
                straight = True

            # Check for three pairs, if so, changes boolean to true
            if sum(1 for count in score_dictionary.values() if count == 2) == 3:
                score += 1500  # Three pairs
                three_pairs = True

        # Perform scoring based on counts
        for num, count in score_dictionary.items():
            # calculates score based on pattern below. 1's worth 1000, everything else is 100
            if count > 2:
                score += num * (count - 2) * (1000 if num == 1 else 100)

            # Scoring pattern for logic of the game, if needed.
            # if count == 6:
            #     if num == 1:
            #         score += (num * 1000) * 4
            #     else:
            #         score += (num * 100) * 4
            # elif count == 5:
            #     if num == 1:
            #         score += (num * 1000) * 3
            #     else:
            #         score += (num * 100) * 3
            # elif count == 4:
            #     if num == 1:
            #         score += (num * 1000) * 2
            #     else:
            #         score += (num * 100) * 2
            # elif count == 3:
            #     if num == 1:
            #         score += (num * 1000) * 1
            #     else:
            #         score += (num * 100) * 1

            # if there is not a set of three pairs or a straight, add additional points for 1's and 5's
            if count < 3 and three_pairs is False and straight is False:
                if num == 1:
                    score += count * 100
                if num == 5:
                    score += count * 50
        return score

    @staticmethod
    def roll_dice(num_of_dice: int) -> tuple[int, ...]:
        """
           Roll a specified number of dice, should not exceed 6 in this game.

           Parameters
           ----------
           num_of_dice : int
               The number of dice to roll.

           Returns
           -------
           tuple
               The result of the dice roll.
           """
        # roll traditional die
        dice_roll = tuple(random.randint(1, 6) for _ in range(0, num_of_dice))

        dice_roll_return = " ".join(map(str, dice_roll))
        print(f'''Rolling {num_of_dice} dice...''')
        print(f'''*** {dice_roll_return} ***''')

        return dice_roll

    @staticmethod
    def create_tuple(current_input: str | int | float) -> tuple[int, ...]:
        """
        Create a tuple from the given input that filters out invalid characters.

        Parameters
        ----------
        current_input : str, int, or float
            The input to convert to a tuple.

        Returns
        -------
        tuple
            The created tuple of only int.
        """
        new_list = [int(x) for x in current_input if x.isdigit()]
        return tuple(new_list)

    @staticmethod
    def get_scorers(last_roll: list) -> list:
        """
       Determine which dice could be used to score points. Only used in the ten_thousand.bot file.

       Parameters
       ----------
       last_roll : list
           The last roll of the dice.

       Returns
       -------
       list
           The dice that contribute to the score.
       """

        counts: dict[int, int] = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0}

        for num in last_roll:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        # account for straights
        if all(counts[num] == 1 for num in range(1, 7)):
            scoring_dice = [num for num, count in counts.items()]
        # Check for three pairs
        elif sum(1 for count in counts.values() if count == 2) == 3:
            scoring_dice = [num for num, count in counts.items() for _ in range(count)]
        else:
            # Checks for all instances of 1's and 5's
            scoring_dice = [num for num, count in counts.items() for _ in range(count) if (num in (1, 5))]
            scoring_dice_2 = []
            # Checks for instances of 3 or above for other dice not 1 & 5
            for num, count in counts.items():
                if count > 2 and num not in scoring_dice:
                    for _ in range(count):
                        scoring_dice_2.append(num)

            scoring_dice.extend(scoring_dice_2)

        return scoring_dice


class NewGame(GameLogic):
    """
    A class to manage a new game instance, inheriting from GameLogic. Manages user inputs.

    Attributes
    ----------
    sim : bool
        Indicates if the game is a simulation.
    """

    def __init__(self):
        """
       Initialize a new NewGame instance.
       """
        super().__init__()
        self.sim = False

    def keep_track_of_dice_roll(self, roller_result: tuple) -> tuple:
        """
        Keep track of the dice roll results.

        Parameters
        ----------
        roller_result : tuple
            The result of the dice roll.

        Returns
        -------
        tuple
            A tuple containing the current dice roll and the counts of each dice value.
        """

        tuple_result = roller_result

        # reset the state of previous roll
        for key in self.dice_just_rolled:
            self.dice_just_rolled[key] = 0
        # assign current dice roll over the last one
        self.dice_roll = tuple_result
        # update the state of the dice just rolled
        for num in tuple_result:
            self.dice_just_rolled[num] += 1

        return self.dice_roll, self.dice_just_rolled

    def keep_new_input(self, new_input: str) -> tuple:
        """
         Process and keep track of new input from the player.

         Parameters
         ----------
         new_input : str
             The input from the player.

         Returns
         -------
         tuple
             A tuple containing the filtered input.
         """
        # filter input to ints and put into a tuple
        input_tuple = self.create_tuple(new_input)

        # reset the input dictionary in class
        for key in self.dice_to_calculate_score:
            self.dice_to_calculate_score[key] = 0

        # add input to dictionary held in class
        for num in input_tuple:
            self.dice_to_calculate_score[num] += 1

        return input_tuple

    def check_for_farkle(self) -> int:
        """
        Check if the current roll is a farkle (no scoring dice).

        Returns
        -------
        int
            The number of dice left to roll, 0 if farkle.
        """
        if self.calculate_score(self.dice_roll) == 0:
            print(f'''
****************************************
**        Zilch!!! Round over         **
****************************************
You banked 0 points in round {self.round}
Total score is {self.score_player_1} points''')
            self.dice_left_to_roll = 0
            return self.dice_left_to_roll
        else:
            pass

    def keep_dice(self, filtered_input_tuple: tuple) -> bool:
        """
         Keep dice based on the player's input.

         Parameters
         ----------
         filtered_input_tuple : tuple
             The filtered input from the player.

         Returns
         -------
         bool
             True if input is invalid, False otherwise.
         """

        # comparison for cheating/typos between what was rolled by game and what was input by user
        # basic comparison: all(dict1[k] == dict2[k] for k in dict1)
        if all(self.dice_to_calculate_score[k] <= self.dice_just_rolled[k] for k in self.dice_to_calculate_score):
            # dice left to roll
            if len(filtered_input_tuple) < 6:
                self.dice_left_to_roll -= len(filtered_input_tuple)
                self.unbanked_points += self.calculate_score(filtered_input_tuple)
                print(
                    f'You have {self.unbanked_points} unbanked points and {self.dice_left_to_roll} dice remaining')
                return False
            # hot dice and the person noticed they had hot dice
            elif len(filtered_input_tuple) == 6:
                self.unbanked_points += self.calculate_score(filtered_input_tuple)
                print(
                    f'You have {self.unbanked_points} unbanked points and {self.dice_left_to_roll} dice remaining')
                return False
            # unforeseen input missed by the tuple filter function create_tuple
            else:
                print('Invalid input format. Please try again.')
                return True
        else:
            # feedback if your input dictionary doesn't match the dice roll dictionary
            print('Cheater!!! Or possibly made a typo...')
            dice_roll_return = " ".join(map(str, self.dice_roll))
            print(f'*** {dice_roll_return} ***')
            return True

    def update_score(self) -> tuple:
        """
        Update the player's score with the unbanked points.

        Returns
        -------
        tuple
            A tuple containing the updated score and unbanked points.
        """
        self.score_player_1 += self.unbanked_points
        print(f'''You banked {self.unbanked_points} points in round {self.round}
    Total score is {self.score_player_1} points''')
        return self.score_player_1, self.unbanked_points

    def increment_round(self) -> int:
        """
        Increment the round number.

        Returns
        -------
        int
            The new round number.
        """
        # increments game round number only
        self.round += 1
        print(f'Starting round {self.round}')
        return self.round

    def change_round(self) -> tuple:
        """
        Change to a new round, resetting relevant attributes.
        Increments round number up +1 using increment_round().

        Returns
        -------
        tuple
            A tuple containing the reset dice left to roll and unbanked points.
        """
        # resets all the values used in a round
        self.dice_left_to_roll = 6
        self.unbanked_points = 0
        self.increment_round()

        return self.dice_left_to_roll, self.unbanked_points






