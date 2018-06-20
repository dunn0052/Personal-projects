# test run for both functions 3 d 6

from s_sum_calc import *
from dice_sum import *
for i in range(10):
    print("Using power series products with " + str(i) + " dice.")
    # first die, second die, how many times to roll second die with 1 roll of first
    chance(mult(make_die(6),make_die(6),i))
    print("Using inclusion/exclusion with " + str(i) + " dice.")
    print_percents(i,6)

