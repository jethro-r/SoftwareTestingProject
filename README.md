Bowling Game Test

This program is a Bowling Game prototype along with some tests to make sure the scoring system and input of rolls is functioning properly.  The game follows the normal rules of bowling, where the player rolls a ball down a lane to knock down pins with 10 frames and mostly 2 rolls per frame. The objective of the game is to score points by knocking down as many pins as possible and to score highest.

Requirements
You will need Python 3 to run this program

Usage
To run the unit tests, simply execute the following command in your terminal:

python Test.py

The output will display the result of each test case and any errors (however there shouldnt be any due to objective of assignment)

Tests
The following tests are included in the TestBowlingGame class:
  test_gutter_game(): Tests the game when all rolls result in 0 pins
  test_all_ones(): Tests the game when each roll scores 1 pin
  test_one_spare(): Tests the game when one spare is rolled
  test_one_strike(): Tests the game when one strike is rolled
  test_perfect_game(): Tests the game when all rolls result in strikes
  test_all_spares(): Tests the game when only spares are rolled
