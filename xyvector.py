import math

con = 'y'

while (con == 'y' ):

    r = eval(input("vector length\n"))

    d = eval(input("vector angle\n"))

    a = math.pi / 180 * d

    x = r * math.cos(a)

    y = r * math.sin(a)

    print(round(x, 3), "," , round(y, 3))

    con = (input("continue y/n?\n"))
