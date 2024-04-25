import pytest
from ten_thousand.flo import diff
from ten_thousand.game import play, first_welcome
from ten_thousand.game import GameLogic

pytestmark = [pytest.mark.version_2]


# @pytest.mark.skip("Pending")
def test_quitter():
    diffs = diff(first_welcome, path="tests/version_2/quitter.sim.txt")
    assert not diffs, diffs


#@pytest.mark.skip("Pending")
def test_one_and_done():
    diffs = diff(first_welcome, path="tests/version_2/one_and_done.sim.txt")
    assert not diffs, diffs


#@pytest.mark.skip("Pending")
def test_single_bank():
    diffs = diff(
        first_welcome, path="tests/version_2/bank_one_roll_then_quit.sim.txt"
    )
    assert not diffs, diffs


#@pytest.mark.skip("Pending")
def test_bank_first_for_two_rounds():
    diffs = diff(
        first_welcome, path="tests/version_2/bank_first_for_two_rounds.sim.txt"
    )
    assert not diffs, diffs