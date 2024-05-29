
# LAB - Class 08

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/maddieamie/ten-thousand/HEAD)

## Project: Ten Thousand Dice Game in Terminal
### Author: Maddie Amelia Lewis

### Versions
Current: Version 3.2

### Links and Resources

Game online: http://www.playonlinedicegames.com/farkle
Rules of the game: https://en.wikipedia.org/wiki/Dice_10000
This is version of the game where you can only bank points once per round, and score is calculated as soon as the dice are set aside.


### Setup

python3 game.py

### Tests

**How do you run tests?**

When you run the main on game.py, you can customize if you are using the MockRoller class or not to simulate test rolls.
When running a particular simulation using the MockRoller class, you can modify the main to run first welcome with the optional parameters changed. If `sim=True` and `sim_number != 0`, then it will create an instance of MockRoller to work in tandem with a new game instance. 

**Any tests of note?**
I also tested it personally as a player, and it seemed to be fine for general inputs. 

**Describe any tests that you did not complete, skipped, etc**
I have not yet created a function test for validate_keepers on the assignment, because I already created a method that accomplishes a similar objective : `create_tuple()` method in the `GameLogic` class.
