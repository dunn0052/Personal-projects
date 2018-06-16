# convoluted dice percentage test

from dice_sum import *

sixdsix = sum_dice()
sixdsix.series = sixdsix.make_die()
sixdsix.mult(sixdsix.make_die(), 5)
sixdsix.chance()
sixdsix.expected_output()
