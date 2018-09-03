# efficient sum calc, all probabilites in O(n^3) because of choose, sum_calc, then find prob
# still no closed formula found, but probably as cheap as you can get
from math import *
from fractions import Fraction
from functools import *
import matplotlib.pyplot as plt

def nCk(n,k):
    return int( reduce(lambda x,y: x*y, (Fraction(n-i, i+1) for i in range(k)), 1))
    # make a list of fractions of (n - k + 1)/(k!). Then take all fractions in the list
    # and multiply them all toegether beginning it all by multiplying by 1. Then
    # reduce that fraction and convert the number back into an integer.


def sum_calc(S,n,m):
    # inclusion/exclusion principal
    # S = sum, n = # of dice, m = # of faces
    return reduce(lambda x,y: x + y ,((-1)**r*nCk((S-1-m*r), n-1)*nCk(n,r) for r in range(int(floor((S-n)/float(m)))+1)), 0)


def prob(n,m):
        return map(lambda i: [i, sum_calc(i,n,m)/float(m**n)], range(n,n*m+1))

def print_percents(n,m,p=4):
    precision = "{:."+str(p)+"%}"
    for terms in prob(n,m):
        print(str(terms[0])+" : "+precision.format(terms[1]))

#n = number of dice, #m = number of sides
def graph_percents(n,m, x = [], y = []):
    p = prob(n,m)
    for e in p:
        x.append(e[0])
        y.append(e[1])
    plt.plot(x, y, 'ro')
    plt.xlabel("Sums")
    plt.ylabel("Percent %")
    plt.show()
