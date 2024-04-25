from random import randint



def default_roller():
    return randint(1, 6, ), randint(1, 6, )


def mock_roller():
    rollss = [(4, 4, 5, 2, 3, 1), (4, 2, 6, 4, 6, 5), (6, 4, 5, 2, 3, 1), (3, 2, 5, 4, 3, 3), (5, 2, 3, 2, 1, 4)]
    return rollss.pop(0)


def play_dice(roller=mock_roller):

    while True:
        print("Enter r to roll or q to quit")
        choice = input("> ")

        if choice == "q":
            print("OK, bye")
            break
        else:
            roll = roller()
            roll_str = ""
            for num in roll:
                roll_str += str(num) + " "
            print(f"*** {roll_str}***")


if __name__ == "__main__":
    rolls = [(4, 4, 5, 2, 3, 1), (3, 3), (2, 2)]

    def mock_roller():
        return rolls.pop(0) if rolls else default_roller()

    play_dice(mock_roller)