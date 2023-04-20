#File 1 (Test.py)

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

  # Initiates the Game (naming convention must be Camel case for this specifically)
  def setUp(self):
    self.game = BowlingGame.BowlingGame()

  # Tests Game with 0 pins
  def test_gutter_game(self):
    self.roll_many(0, 20)
    self.assertEqual(self.game.score(), 0)

  # Tests Game with 1 pin per roll
  def test_all_ones(self):
    self.roll_many(1, 20)
    self.assertEqual(self.game.score(), 20)

  # Tests Game with 1 spare
  def test_one_spare(self):
    self.game.roll(5)
    self.game.roll(5)
    self.game.roll(3)
    self.roll_many(0, 17)
    self.assertEqual(self.game.score(), 16)

  # Tests Game with 1 strike
  def test_one_strike(self):
    self.game.roll(10)
    self.game.roll(4)
    self.game.roll(3)
    self.roll_many(0, 16)
    self.assertEqual(self.game.score(), 24)

  # Tests Game with 10 strikes + 2 extra strikes
  def test_perfect_game(self):
    self.roll_many(10, 12)
    self.assertEqual(self.game.score(), 300)

  # Tests Game with only spare rolls
  def test_all_spares(self):
    self.roll_many(5, 21)
    self.assertEqual(self.game.score(), 150)

  # function that rolls multiple times for quick testing
  def roll_many(self, pins, rolls):
    for i in range(rolls):
      self.game.roll(pins)
			



		

