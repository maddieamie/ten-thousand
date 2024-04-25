import random
import ast


class GameLogic:

    def __init__(self):
        self.amount_of_dice = range(0, 6 + 1)
        self.dice_sides = range(1, 6 + 1)
        self.dice_set_aside_to_score = 0
        self.dice_left_to_roll = 6
        self.dice_just_rolled = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }
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
    def calculate_score(dice_roll_tuple):
        score = 0
        three_pairs = False
        straight = False

        if len(dice_roll_tuple) > 6:
            raise ValueError("Invalid dice value encountered")

        score_dictionary = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }

        # Iterate through the tuple and update counts
        for num in dice_roll_tuple:
            if num in score_dictionary:
                score_dictionary[num] += 1
            else:
                raise ValueError("Invalid dice value encountered")

            if all(score_dictionary[num] == 1 for num in range(1, 7)):
                score += 1500  # Straight
                straight = True

            # Check for three pairs
            if sum(1 for count in score_dictionary.values() if count == 2) == 3:
                score += 1500  # Three pairs
                three_pairs = True

        # Perform scoring based on counts
        for num, count in score_dictionary.items():
            if count == 6:
                if num == 1:
                    score += (num * 1000) * 4
                else:
                    score += (num * 100) * 4
            elif count == 5:
                if num == 1:
                    score += (num * 1000) * 3
                else:
                    score += (num * 100) * 3
            elif count == 4:
                if num == 1:
                    score += (num * 1000) * 2
                else:
                    score += (num * 100) * 2
            elif count == 3:
                if num == 1:
                    score += 1000
                else:
                    score += (num * 100)

            if count < 3 and three_pairs is False and straight is False:
                if num == 1:
                    score += count * 100
                if num == 5:
                    score += count * 50

        # print(score_dictionary)
        # print(score)

        return score

    def roll_dice(self, num_of_dice):
        # reset previous dice roll
        for key in self.dice_just_rolled:
            self.dice_just_rolled[key] = 0
        # number of dice being rolled to return to user
        dice_num = num_of_dice
        # roll dice
        dice_roll = tuple(random.randint(1, 6) for _ in range(0, dice_num))
        # keep track of dice last rolled for logic later
        for num in dice_roll:
            self.dice_just_rolled[num] += 1

        dice_roll_return = " ".join(map(str, dice_roll))

        return print(f'''Rolling {dice_num} dice...
*** {dice_roll_return} ***''')

    def increment_round(self):
        # increments game round number only
        self.round += 1
        return print(f'Starting round {self.round}')

    def change_round(self):
        # resets all the values used in a round
        self.dice_set_aside_to_score = 0
        self.dice_left_to_roll = 6
        self.unbanked_points = 0
        self.increment_round()

    @staticmethod
    def create_tuple(current_input):
        new_list = [int(x) for x in current_input if x.isdigit()]
        return tuple(new_list)

    def keep_dice(self, input):
        # this line needs to be refined for different inputs
        # comparison to rolled dice needs to come here as well
        input_tuple = self.create_tuple(input)

        for num in input_tuple:
            self.dice_to_calculate_score[num] += 1
        # if self.dice_to_calculate_score.items() <= self.dice_just_rolled.items()
        if len(input_tuple) < 6:
            self.dice_set_aside_to_score += len(input_tuple)
            self.dice_left_to_roll -= len(input_tuple)
            self.unbanked_points += self.calculate_score(input_tuple)
            if self.unbanked_points == 0:
                # farkle function
                return print('No points scored! Next round.')
            else:
                return print(f'You have {self.unbanked_points} unbanked points and {self.dice_left_to_roll} dice remaining')
        elif len(input_tuple) == 6:
            self.unbanked_points += self.calculate_score(input_tuple)
            return print(f'You have {self.unbanked_points} unbanked points and {self.dice_left_to_roll} dice remaining')
        else:
            return print('Invalid input format. Please try again.')

    def update_score(self):
        self.score_player_1 += self.unbanked_points
        return print(f'''You banked {self.unbanked_points} points in round {self.round}
Total score is {self.score_player_1} points''')


    # change return on update score/ roll again after using all 6 dice the first time
    # change round and reset when user rolls no scoring dice (unbanked_points = 0?)





