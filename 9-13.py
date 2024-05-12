import random

class Die:
  """
  A class to represent a die with a certain number of sides.
  """
  def __init__(self, num_sides=6):
    """
    Initializes the die with a specified number of sides.

    Args:
      num_sides: The number of sides on the die (default is 6).
    """
    self.num_sides = num_sides

  def roll_die(self):
    """
    Rolls the die and prints a random number between 1 and the number of sides.
    """
    print(random.randint(1, self.num_sides))

# Create a 6-sided die and roll it 10 times
six_sided_die = Die()
for _ in range(10):
  six_sided_die.roll_die()

# Create a 10-sided die and roll it 10 times
ten_sided_die = Die(10)
for _ in range(10):
  ten_sided_die.roll_die()

# Create a 20-sided die and roll it 10 times
twenty_sided_die = Die(20)
for _ in range(10):
  twenty_sided_die.roll_die()
