import random


class GameLogic:
    def __init__(self):
        self.amount_of_dice = range(0, 6 + 1)
        self.dice_sides = range(1, 6 + 1)
        self.dice_set_aside_to_score = 0
        self.dice_in_limbo = 0
        self.score_player_1 = 0
        self.score_player_2 = 0

    @staticmethod
    def calculate_score(dice_roll_tuple):
        score = 0
        three_pairs = False

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

            if count < 3 and three_pairs is False:
                if num == 1:
                    score += count * 100
                if num == 5:
                    score += count * 50

        print(score_dictionary)
        print(score)

        return score

    @staticmethod
    def roll_dice(num_of_dice):
        return tuple(random.randint(1, 6) for _ in range(0, num_of_dice))
