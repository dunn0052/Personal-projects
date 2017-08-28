#mancala array

def pick(j, m):
    print(m , "P")
    if(j[m] != 0):
        n = j[m]
        j[m] = 0
        k = move(j, (m+1)%14, n)
    return k

def move(j, m, n):
    if(n == 1 and j[m] != 0 and (m != 0 or m != 7)):
        j[m] += 1
        pick(j,m)
    elif(n != 0):
        print(m, "M")
        j[m] += 1
        move(j, (m+1)%14, n-1)
    else:
        print("end")
        return (m-1)%14

def strat(j):
    s = []
    best = 0
    best_move = 0
    for i in range (1,7):
        s.append(j)
        end = pick(s[i-1],i)
        if(end == 7):
            s.append(j)
        '''else:
            k = s[i][7] - j[7]
            if(k > best):
                best = k
                best_move = i
    '''
    return s

def again(s):
        while(s and s[len(s) - 1][7] < 23):
            r = s.pop()
            strat(r)
        
        
M = [0,4,4,4,4,4,4,0,4,4,4,4,4,4]
print(pick(M,3))
