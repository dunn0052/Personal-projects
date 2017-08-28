import math

con = 'y'

while (con == 'y' ):
    x = eval(input("enter x component\n"))

    y = eval(input("enter y component \n"))

    r = math.hypot(x, y)

    a = math.atan(y/x)

    d = 180 / math.pi * a

    

    print(round(r, 2), ",", round(d, 2))

    con = input("Continue y/n\n?")
