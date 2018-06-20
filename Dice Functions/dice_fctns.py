#dice functions


def factorial(n, prod = 1):
    if(n < 0):
        print("can't be negative")
        #for now
        return
    elif(n%1 > 0): 
        print("must be whole number")
        return    
    if(n == 0):
        return 1
    if (n > 1):
        #non tail recursion
        prod *= n
        return factorial(n-1, prod)
        #recursive iteration
    else:
        return prod

def way_better_factorial(n):
    if(n > 1 and n%1 == 0):
        prod = 1
        if n == 0:
            return prod
        while(n > 1):
            prod *= n
            n -= 1
        return prod
    else:
        print("can't do that")
        return

    
def choose(n, r):
    return factorial(n)//factorial(r)//factorial(n-r)
    #nCr

def pick(n, r):
    return factorial(n)//factorial(n - r)
    #nPr

def binomial_at_least(n,k,p):
    #n = number of tries
    #k = number of successes
    #p = probablity of success per try
    prob = 0
    while(n>=k):
        prob = prob + choose(n,k)*(p)**k*(1-p)**(n-k)
        k = k + 1
    return prob
def binomial_at_least_map(n,k,p):
    return



def WOD(n,k):
    #Chances of rolling k successes with n dice in WOD
    print("Rolling",n,"dice with",k,"successe(s)")
    print(round(binomial_at_least(n,k,0.3)*100),  "%")



