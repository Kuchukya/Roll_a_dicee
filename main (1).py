import random


def roll_a_dice():
  dice_1 = random.randint(1, 6)
  dice_2 = random.randint(1, 6)
  return dice_1 + dice_2


def play_game():
  roll = roll_a_dice()
  if roll == 7 or roll == 11:
    print(f"You win! The sum of the dice is {roll}.")
    return True

  elif roll == 2 or roll == 3 or roll == 12:
    print(f"You lose. The sum of the dice is {roll}.")
    return False

  else:
    print(f"The sum of the dice is {roll}. This is your goal number.")
    goal = roll
    while True:
      roll = roll_a_dice()
      if roll == goal:
        print(f"You win! The sum of the dice is {roll}.")
        return True
      elif roll == 7:
        print(f"You lose. The sum of the dice is {roll}.")
        return False
      else:
        print(f"The sum of the dice is {roll}. Roll again.")


play_game()
