#prime_factors, GCF, Pythagorean triples
import math

def factorize(a,n,k=2):
    #prime factors of n stored in a[]
    if(not (n%k)):

        #if prime divides, add to list
        a.append(k)
        n=n/k
        factorize(a,n,k)
    elif(k<= math.sqrt(n)):
        #try next with limit
        factorize(a,n,k+1)
        
    elif(n>1):
        #adds last factor
        a.append(int(n))
        


def GCF(a,b,c):
    #Finds the greatest common factor between 3 numbers
    d = []
    e = []
    f = []
    factorize(d,a)
    factorize(e,b)
    factorize(f,c)
    
    #find largest common prime factor
    largest_factor = []
    largest_factor.append(max(d))
    largest_factor.append(max(e))
    largest_factor.append(max(f))
    k = max(largest_factor)

    #store and remove each common prime factor
    GCF_list = []
    for i in range(k+1):
        while(i in d and i in e and i in f):
            GCF_list.append(i)
            d.remove(i)
            e.remove(i)
            f.remove(i)
            
    #multiply common factors for GCF
    product = 1
    for x in GCF_list:
        product *= x
    return product

def pythagorean_triple(u,v):
    #function for possible pythagorean triples
    a = []

    #hypotenuse
    a.append(u**2 + v**2)
    #side
    a.append(u**2 - v**2)
    #side
    a.append(2*u*v)

    #remove negative values
    if(a[0] < 1 or a[1] < 1 or a[2] < 1):
        return
    return a


#prints relatively prime tuples in order of smallest side
k = []
for i in range(100):
    j = 0

    n = i
    while(n > 0):
        if(pythagorean_triple(i,n) != None):
            q = []
            q = pythagorean_triple(i,n)
            q.sort()
            g = GCF(q[0],q[1],q[2])
            q[:] = [int(x/g) for x in q]
            if(q in k):
                break
            k.append(q)
            j= j + 1
        n = n-1
k.sort()
for i in range(len(k)):
    print(k[i])
print(len(k), "total")
