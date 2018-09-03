#import matplotlib.pyplot as plt
import crw
import math

def xfactor(l):
    m = {1: 9, 3: 3, 7: 7, 9: 1}
    y = []
    for p in l:
        decimal = p/10
        whole = math.floor(decimal)
        last = int(round((decimal - whole)*10))
        y.append(int((int(p*m[last]+1)/10)))
    return y

primes = crw.getData("primeclean")
#print(primes)
y = xfactor(primes)
z = zip(primes, y)
z = list(z)
print(len(z))
#plt.plot(primes[:1000],y)

#plt.axis('off')
#plt.show()
