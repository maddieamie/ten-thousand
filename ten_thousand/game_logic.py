import random
import ast


class GameLogic:

    def __init__(self):
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

    @staticmethod
    def roll_dice(num_of_dice):
        # roll dice
        dice_roll = tuple(random.randint(1, 6) for _ in range(0, num_of_dice))
        # keep track of dice last rolled for logic later

        dice_roll_return = " ".join(map(str, dice_roll))
        print(f'''Rolling {num_of_dice} dice...
        *** {dice_roll_return} ***''')

        return dice_roll

    @staticmethod
    def create_tuple(current_input):
        new_list = [int(x) for x in current_input if x.isdigit()]
        return tuple(new_list)


class NewGame(GameLogic):

    def __init__(self):
        super().__init__()
        self.sim = False

    def keep_track_of_dice_roll(self, roller_result):

        tuple_result = roller_result

        # print('prev roll:', self.dice_just_rolled)
        for key in self.dice_just_rolled:
            self.dice_just_rolled[key] = 0

        self.dice_roll = tuple_result

        for num in tuple_result:
            self.dice_just_rolled[num] += 1

        return self.dice_roll, self.dice_just_rolled

    def keep_new_input(self, new_input):
        # filter input and put into a tuple
        input_tuple = self.create_tuple(new_input)

        # reset the input dictionary in class
        for key in self.dice_to_calculate_score:
            self.dice_to_calculate_score[key] = 0

        # add input to dictionary held in class
        for num in input_tuple:
            self.dice_to_calculate_score[num] += 1

        # print(self.dice_to_calculate_score)

        return input_tuple

    def check_for_farkle(self):
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

    def keep_dice(self, filtered_input_tuple):

        # comparison for cheating/typos
        # print(self.dice_to_calculate_score)
        # print(self.dice_just_rolled)
        # all(dict1[k] == dict2[k] for k in dict1)
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

    def update_score(self):
        self.score_player_1 += self.unbanked_points
        print(f'''You banked {self.unbanked_points} points in round {self.round}
    Total score is {self.score_player_1} points''')
        return self.score_player_1, self.unbanked_points

    def increment_round(self):
        # increments game round number only
        self.round += 1
        print(f'Starting round {self.round}')
        return self.round

    def change_round(self):
        # resets all the values used in a round
        self.dice_left_to_roll = 6
        self.unbanked_points = 0
        self.increment_round()

        return self.dice_left_to_roll, self.unbanked_points






