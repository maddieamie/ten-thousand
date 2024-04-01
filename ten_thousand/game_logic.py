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

        # Check for specific combinations when there are six dice rolled
        if len(dice_roll_tuple) == 6:
            if sorted(dice_roll_tuple) == [1, 2, 3, 4, 5, 6]:
                score += 1500  # Straight
            elif dice_roll_tuple.count(1) == 6:
                score += 4000  # Six of a Kind (1)
            elif dice_roll_tuple.count(2) == 6:
                score += 800  # Six of a Kind (2)
            elif dice_roll_tuple.count(3) == 6:
                score += 1200  # Six of a Kind (3)
            elif dice_roll_tuple.count(4) == 6:
                score += 1600  # Six of a Kind (4)
            elif dice_roll_tuple.count(5) == 6:
                score += 2000  # Six of a Kind (5)
            elif dice_roll_tuple.count(6) == 6:
                score += 2400  # Six of a Kind (6)
            elif sum(num // 2 for num in Counter(dice_roll_tuple).values()) == 3:
                score += 1500  # Three Pairs

        # If none of the above conditions are true, check for other combinations
        if score == 0:
            for i in range(1, 7):
                # Groups of 5
                if dice_roll_tuple.count(i) == 5:
                    if i == 1:
                        score += 3000
                    else:
                        score += (i * 100) * 3
                    break
                # Groups of 4
                elif dice_roll_tuple.count(i) == 4:
                    if i == 1:
                        score += 2000
                    else:
                        score += (i * 100) * 2
                    break

            # Count triples and two sets of triples
            triple_count = 0
            for j in range(1, 7):
                if dice_roll_tuple.count(j) == 3 and triple_count < 2:
                    if j == 1:
                        score += 1000
                    else:
                        score += j * 100
                    triple_count += 1

        if score == 0:
            # Separate handling for additional ones and fives
            score += dice_roll_tuple.count(1) * 100
            score += dice_roll_tuple.count(5) * 50

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
