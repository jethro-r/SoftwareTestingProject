#File 2 (BowlingGame.py)

class BowlingGame:
  # initial game variables
  def __init__(self):
    self.rolls = []

  # function to add the number of pins hit in a roll to list
  def roll(self, pins_hit):
    self.rolls.append(pins_hit)

  # score function that works out frames and bonus scoring rolls
  def score(self):
    result = 0
    roll_index = 0 # roll index is track which roll the system is at. 
    for frame_index in range(10):
      if self.is_strike(roll_index):
        result += self.bonus_rolls_score(roll_index)
        roll_index += 1 # +1 because there is no second shot, so next number in list will be the next frame
      elif self.is_spare(roll_index):
        result += self.bonus_rolls_score(roll_index)
        roll_index += 2 # +2 because 'isSpare()' has checked for spare already, so no need to go to next number
      else:
        result += self.frame_score(roll_index)
        roll_index += 2
    return result

  # checks if Number of pins hit is 10, if so it counts as a strike
  def is_strike(self, roll_index):
    return self.rolls[roll_index] == 10
  
  # checks if Number of pins over two rolls is 10, if so it counts as a spare
  def is_spare(self, roll_index):
    return self.rolls[roll_index] + self.rolls[roll_index + 1] == 10
  
  # both Strikes and Spares have the same scoring system, so merged both into a function that gets the next two scores to get the total for that frame
  def bonus_rolls_score(self, roll_index):
    return self.rolls[roll_index] + self.rolls[roll_index + 1] + self.rolls[roll_index + 2]

  # normal frame scoring, first plus second rolls = score for frame
  def frame_score(self, roll_index):
    return self.rolls[roll_index] + self.rolls[roll_index + 1]
