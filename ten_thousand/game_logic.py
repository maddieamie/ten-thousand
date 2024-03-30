from collections import Counter
import sys as _sys
import random

class GameLogic:
    def __init__(self):
        self.amount_of_dice = range(0, 6 + 1)
        self.dice_sides = range(1, 6 + 1)
        self.dice_set_aside_to_score = 0
        self.dice_in_limbo = 0
        self.score_player_1 = 0
        self.score_player_2 = 0



# for each set of dice set aside, the score is calculated then
# additional rolls do not add to score, group scores must be rolled simultaneously
    @staticmethod
    def calculate_score(dice_roll_tuple):
        score = 0

        if dice_roll_tuple.issubset([1, 2, 3, 4, 5, 6]):
            #if dice_roll_tuple has 1 of each type for a straight
            score += 1500
        if sum(num//2 for num in Counter(dice_roll_tuple).values()) == 3:
            # if the sum of the pairs is 3 pairs
            score += 750
        if dice_roll_tuple.count(1) == 3:
            score += 1000
        if dice_roll_tuple.count(2) == 3:
            score += 200
        if dice_roll_tuple.count(3) == 3:
            score += 300
        if dice_roll_tuple.count(4) == 3:
            score += 400
        if dice_roll_tuple.count(5) == 3:
            score += 500
        if dice_roll_tuple.count(6) == 3:
            score += 600
        elif dice_roll_tuple.count(1) == 6:
            score += 4000
        elif dice_roll_tuple.count(2) == 6:
            score += 800
        elif dice_roll_tuple.count(3) == 6:
            score += 1200
        elif dice_roll_tuple.count(4) == 6:
            score += 1600
        elif dice_roll_tuple.count(5) == 6:
            score += 2000
        elif dice_roll_tuple.count(6) == 6:
            score += 2400
        elif dice_roll_tuple.count(1) == 5:
            score += 3000
        elif dice_roll_tuple.count(2) == 5:
            score += 600
        elif dice_roll_tuple.count(3) == 5:
            score += 900
        elif dice_roll_tuple.count(4) == 5:
            score += 1200
        elif dice_roll_tuple.count(5) == 5:
            score += 1500
        elif dice_roll_tuple.count(6) == 5:
            score += 1800
        elif dice_roll_tuple.count(1) == 4:
            score += 2000
        elif dice_roll_tuple.count(2) == 4:
            score += 400
        elif dice_roll_tuple.count(3) == 4:
            score += 600
        elif dice_roll_tuple.count(4) == 4:
            score += 800
        elif dice_roll_tuple.count(5) == 4:
            score += 1000
        elif dice_roll_tuple.count(6) == 4:
            score += 1200
        else:
            for dice_roll in dice_roll_tuple:
                if dice_roll == 1:
                    score += 100
                if dice_roll == 5:
                    score += 50
                if dice_roll != 1 or dice_roll != 5:
                    score += 0
        return score

    @staticmethod
    def roll_dice(num_of_dice):
        return tuple(random.randint(1, 6) for _ in range(0, num_of_dice))

    # @staticmethod
    # def roll_dice(num_dice):
    #     # return tuple(random.randint(1, 6) for _ in range(num_dice))
    #     dice_values = []
    #     for _ in range(num_dice):
    #         value = random.randint(1, 6)
    #         dice_values.append(value)
    #     return tuple(dice_values)

# need method to determine whose turn it is, so the score goes to that player & turn eventually ends
# need method to determine in loop that allows users to pick dice to set aside,
# which sends the set aside dice to the calculate score method, then to limbo
# if player rolls all 6 dice with scoring dice, add to player's limbo score to total score
# if player rolls only not-scoring dice, then lose all points in limbo, next player turn
# players cannot use multiple rolls to acculumate scoring dice, i.e. if you set a