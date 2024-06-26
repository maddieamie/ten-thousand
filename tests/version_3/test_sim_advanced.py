import pytest
from ten_thousand.flo import diff
from ten_thousand.game import first_welcome



pytestmark = [pytest.mark.version_3]


# @pytest.mark.skip("Pending")
def test_repeat_roller():
    """Allow setting aside scoring dice and rolling the rest
    """
    diffs = diff(first_welcome, path="tests/version_3/repeat_roller.sim.txt")
    assert not diffs, diffs


@pytest.mark.skip("Pending")
def test_hot_dice():
    """When all dice are used without a zilch
    then user gets 6 fresh dice and continues turn.
    """
    diffs = diff(first_welcome, path="tests/version_3/hot_dice.sim.txt")
    assert not diffs, diffs


@pytest.mark.skip("Pending")
def test_cheat_and_fix():
    """Cheating (or typos) should not be allowed.
    Therefore the user's input must be validated
    If invalid prompt user for re-entry
    """

    diffs = diff(first_welcome, path="tests/version_3/cheat_and_fix.sim.txt")
    assert not diffs, diffs


@pytest.mark.skip("Pending")
def test_zilcher():
    """
    No scoring dice results in a 'zilch'
    which wipes away shelved points
    and ends turn
    """

    diffs = diff(first_welcome, path="tests/version_3/zilcher.sim.txt")
    assert not diffs, diffs