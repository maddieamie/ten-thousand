
class MockRoller:
    """
       A class to simulate predefined dice rolls for the Ten Thousand game.

       Attributes
       ----------
       dice_just_rolled_mock : dict
           A dictionary to keep track of the count of each dice value just rolled.
       dice_roll_mock : tuple
           A tuple to store the current dice roll.
       rolls1 : list of tuples
           Predefined dice rolls for the first simulation scenario: version_3/cheat_and_fix.sim.txt
       rolls2 : list of tuples
           Predefined dice rolls for the second simulation scenario: version_2/bank_first_for_two_rounds.sim.txt
       rolls3 : list of tuples
           Predefined dice rolls for the third simulation scenario: version_2/bank_one_roll_then_quit.sim.txt
       rolls4 : list of tuples
           Predefined dice rolls for the fourth simulation scenario: version_2/one_and_done.sim.txt
       rolls5 : list of tuples
           Predefined dice rolls for the fifth simulation scenario: version_3/hot_dice.sim.txt
       rolls6 : list of tuples
           Predefined dice rolls for the sixth simulation scenario: version_3/repeat_roller.sim.txt
       rolls7 : list of tuples
           Predefined dice rolls for the seventh simulation scenario: version_3/zilcher.sim.txt
       """
    def __init__(self):
        """
       Initialize a new MockRoller instance.
       """
        self.dice_just_rolled_mock = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0
        }
        self.dice_roll_mock = ()
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
        """
       Simulate a dice roll based on the given roll number.

       Parameters
       ----------
       roll_number : int
           The simulation scenario to use for the dice roll.

       Returns
       -------
       tuple
           The current simulated dice roll.
       """
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

        # reset previous dice rolls in MockRoller state

        for key in self.dice_just_rolled_mock:
            self.dice_just_rolled_mock[key] = 0

        # roll fake dice
        self.dice_roll_mock = roll_list.pop(0)
        # updates state of MockRoller to bubble up to NewGame
        dice_num = len(self.dice_roll_mock)

        #  updates state of MockRoller to bubble up to NewGame
        for num in self.dice_roll_mock:
            self.dice_just_rolled_mock[num] += 1

        dice_roll_return = " ".join(map(str, self.dice_roll_mock))
        print(f'''Rolling {dice_num} dice...
*** {dice_roll_return} ***''')
        return self.dice_roll_mock



