# convoluted dice percentage test

from dice_sum import *

twelve = dice_gen(12)
y = sum_dice(twelve.die)
y.mult(twelve.die, 4)
y.chance()
