# use dynamic programming
# finding combinations using multinomial coefficients by power series products
# mult can be used to combine any 2 dice
# die face[[how many faces have this number, what number is on that face],...]
# example regular d 6 [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6]]
# house on the hill die [[2,0],[2,1],[2,2]]





def mult(x, y, n = 1):
    # x, y nested lists such that [[coef1,deg1], [coef2,deg2],...]
    # = coef1*x^deg1 + coef2*x^deg2
    product = []
    for i in range(n-1): # because original x counts as die 1
        for term in x:
            for pterm in y:
                # multinomial expansion
                product.append([term[0] * pterm[0], term[1] + pterm[1]])
        x = combine(product) # make x new thing to be multiplied by original y
        product = [] # reset product so that a new collection of x * y can be made
    return x 
    

def combine(x):
    combination = []
    # sort by deg
    x.sort(key = lambda x: x[1])
    first = x[0][1] # lowest deg
    coef = 0
    for term in x:
        if term[1] == first:
            # add term coef if same deg
            coef += term[0]
        elif term[1] != first:
            # if next deg is found
            # add combined coef with its deg
            combination.append([coef, first])
            # get that coef
            coef = term[0]
            # get that next deg
            first = term[1]
    # missing the last term? oh well it's fixed now.
    combination.append([coef, first])
    return combination

def chance(p, n = 4):
    total = float(sum(x[0] for x in p))
    for coef in p:
        # look at this backaswwardness for precision
        precision = "{:."+ str(n) + "%}"
        print(str(coef[1]) + " : " + precision.format(coef[0]/total))

def make_die(sides = 6):
    die = []
    for i in range(1, sides+1):
        # [face #, how many faces on a die]
        die.append([1,i])
    return die

def expected_output(p):
    total = float(sum(x[0] for x in p))
    out = 0
    for coef in p:
        out += coef[1]*coef[0]/total
    print("Expected output: " + "{:.4}".format(out))
    return out
