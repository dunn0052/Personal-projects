# efficient sum calc, all probabilites in O(n^3) because of choose, sum_calc, then find prob
# still no closed formula found, but probably as cheap as you can get
from math import *
from operator import mul
from fractions import Fraction

def nCk(n,k):
    # from https://stackoverflow.com/questions/3025162/statistics-combinations-in-python
    return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1))


def sum_calc(S,n,m):
    # S = sum, n = # of dice, m = # of faces
    total=0
    # from https://www.quora.com/How-do-you-find-the-number-of-ways
    # -the-sum-of-k-dice-rolls-equals-S-for-an-n-sided-fair-die
    for r in range(int(floor((S-n)/float(m)))+1):
        total += (-1)**r*nCk((S-1-m*r), n-1)*nCk(n,r)
    return total

def prob(n,m):
    percents = []
    sample_space = float(m**n)
    for i in range(n,n*m+1):
        percents.append([i, sum_calc(i,n,m)/sample_space])
    return percents

def print_percents(n,m,p=4):
    precision = "{:."+str(p)+"%}"
    for terms in prob(n,m):
        print(str(terms[0])+" : "+precision.format(terms[1]))
