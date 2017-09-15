#Created by Kevin Dunn, PAL facilitator 09/13/17
#PAL group randomizer - This function creates random groups for PAL sessions
#1. Have students print name on numbered attendence sheet
#2. Run program with number of students and how many you want per group
#3. Organize groups by the program results

import random

#n is number of people in class and m is number per each group

def randomizer(n, m):
    a = []
    for i in range(n):
        a.append(i)
        
    random.shuffle(a)
    
    k = 0
    j = n%m
    while(k < n//m):
        print("group", k + 1)
        for i in range(m):
            print(a[m*k + i] + 1)
            if(j != 0 and i == m - 1):
                print(a[n - j] + 1)
                j = j - 1
        k = k + 1
        print("")


randomizer(20,3)
