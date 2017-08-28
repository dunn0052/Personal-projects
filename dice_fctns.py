#dice functions


def factorial(n):
    if(n < 0):
        print("can't be negative")
        return
    elif(n%1 > 0): 
        print("must be whole number")
        return
        
    if(n == 0):
        return 1
    if (n > 1):
        n = factorial(n-1) * n
        return n
        #recursive iteration
    else:
        return n

    
def choose(n, r):
    return factorial(n)//factorial(r)//factorial(n-r)
    #nCr

def pick(n, r):
    return factorial(n)//factorial(n - r)
    #nPr

def binomial_at_least(n,k,p):
    prob = 0
    while(n>=k):
        prob = prob + choose(n,k)*(p)**k*(1-p)**(n-k)
        k = k + 1
    return prob



def WOD(n,k):
    #Chances of rolling k successes with n dice in WOD
    print("Rolling",n,"dice with",k,"successe(s)")
    print(round(binomial_at_least(n,k,0.3)*100),  "%")



