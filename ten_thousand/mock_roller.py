class MockRoller:

    def __init__(self):
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

    def mock_roller(self, roll_number):
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

        return roll_list.pop(0) if roll_list else print("boop, out of rolls")