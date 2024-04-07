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


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((1,), 100),
        ((1, 1), 200),
        ((2, 2, 1, 1), 200),
        ((3, 5, 1, 1), 250),
        ((1, 1, 3, 4, 5), 250),
        ((5, 5, 1, 1, 1, 1), 2100),
        ((5,), 50),
        ((5, 5), 100),
        ((1, 5, 5), 200),
        ((5, 1, 1), 250),
        ((5, 5, 5, 1), 600),
        ((5, 5, 1, 1), 300),
        ((5, 5, 1, 1, 6), 300),
        ((1, 1, 1, 5), 1050),
        ((5, 5, 5, 1, 2), 600),
        ((5, 5, 5, 1, 6, 3), 600),
        ((3, 3, 3, 1), 400),
        ((3, 3, 3, 3, 5), 650),
        ((3, 3, 3, 3, 3, 1), 1000),
        ((4, 3, 2, 1, 5, 4), 150),
        ((1, 1, 5, 5, 4, 3), 300),
        ((2, 2, 3, 3, 4, 6), 0),
        ((1, 1, 5, 5, 6, 6), 1500),
        ((1, 1, 1, 5, 5, 5), 1500),
        ((1, 1, 1, 3, 3, 3), 1300),
        ((2, 2, 2, 5, 5, 5), 700)
    ],
)
def test_edge_cases_in_range_one_and_five(test_input, expected):
    actual = GameLogic.calculate_score(test_input)
    assert actual == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ((1, 1, 5, 5, 6, 6), 1500),
        ((2, 2, 2, 2, 3, 3), 400),
        ((5, 5, 5, 5, 3, 3), 1000),
        ((2, 2, 4, 4, 6, 6), 1500),
        ((1, 1, 1, 1, 3, 3), 2000),
        ((3, 3, 3, 3, 3, 3), 1200)
    ],
)
def test_edge_cases_in_pairs(test_input, expected):
    actual = GameLogic.calculate_score(test_input)
    assert actual == expected
