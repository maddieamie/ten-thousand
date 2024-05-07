from ten_thousand.game_logic import GameLogic


class MockRoller(GameLogic):

    # def __init__(self, dice_just_rolled, dice_to_calculate_score, dice_roll):
    def __init__(self, dice_just_rolled, dice_roll):
        super().__init__()
        self.dice_just_rolled_mock = dice_just_rolled
        self.dice_roll_mock = dice_roll
        # cheat and fix sim
        self.rolls1 = [(5, 2, 3, 5, 4, 2), (5, 2, 3, 5, 4, 2)]
        # bank first for two rounds sim
        self.rolls2 = [(3, 2, 5, 4, 3, 3), (5, 2, 3, 2, 1, 4), (6, 6, 5, 4, 2, 1)]
        # bank one roll then quit sim
        self.rolls3 = [(4, 2, 6, 4, 6, 5), (6, 4, 5, 2, 3, 1)]
        # one and done sim
        self.rolls4 = [(4, 4, 5, 2, 3, 1)]
        # hot dice sim
        self.rolls5 = [(2, 3, 1, 3, 1, 2), (4, 1, 4, 4, 3, 4), (3, 2, 3, 2, 1, 4)]
        # repeat roller sim
        self.rolls6 = [(2, 3, 1, 3, 4, 2), (4, 2, 4, 4, 6), (3, 2, 3, 2, 1, 4)]
        # zilch sim
        self.rolls7 = [(1, 2, 5, 1, 2, 1), (4, 4), (1, 1, 2, 5, 1, 6)]

        # so, when I call mock_roller in the game, I can call which sim
        # Can I change up test_sim to put in the roll_number param for me & use
        # mock_roller without hard-coding it in game_logic for the sim?

    def mock_roller(self, roll_number):
        # ideally, this function updates the state of the lists in the MockRoller class
        # AND uses the state of the GameLogic to update the dice_roll logic implemented
        # in the regular roll_dice function
        roll_list = []
        if roll_number == 1:
            roll_list = self.rolls1
        elif roll_number == 2:
            roll_list = self.rolls2
        elif roll_number == 3:
            roll_list = self.rolls3
        elif roll_number == 4:
            roll_list = self.rolls4
        elif roll_number == 5:
            roll_list = self.rolls5
        elif roll_number == 6:
            roll_list = self.rolls6
        elif roll_number == 7:
            roll_list = self.rolls7

        # reset previous dice rolls in GameLogic State

        for key in self.dice_just_rolled_mock:
            self.dice_just_rolled_mock[key] = 0

        # for key in self.dice_to_calculate_score:
        #     self.dice_to_calculate_score[key] = 0

        # roll fake dice, updates state of MockRoller list
        self.dice_roll_mock = roll_list.pop(0)
        # updates state of GameLogic
        dice_num = len(self.dice_roll_mock)

        # keep track of dice last rolled for GameLogic later
        for num in self.dice_roll_mock:
            self.dice_just_rolled_mock[num] += 1

        dice_roll_return = " ".join(map(str, self.dice_roll_mock))

        return print(f'''Rolling {dice_num} dice...
*** {dice_roll_return} ***''')



