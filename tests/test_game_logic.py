import pytest
from ten_thousand.game_logic import GameLogic

@pytest.mark.parametrize(
    "num_dice,expected_length",
    [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
    ],
)
def test_all_valid_dice_rolls(num_dice, expected_length):
    roll = GameLogic.roll_dice(num_dice)
    assert len(roll) == expected_length
    for value in roll:
        assert 1 <= value <= 6