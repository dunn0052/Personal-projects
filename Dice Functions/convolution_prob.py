# dice probability using recursive discrete convolution

#n = number of dice, k = sum total, f = number of die faces
def conv(n, k, f):
    s = 0
    #safety measures
    if k < n:
        print("Cannot produce", k,"with", n,"dice")
        return s
    if n == 1 or n == k:
        return 1#/f
    for j in range(max(1,k-f*(n-1)), min(f+1, k-(n-1)+1)):
        s += conv(n-1, k-j, f) * conv(1, j, f)
    return s
