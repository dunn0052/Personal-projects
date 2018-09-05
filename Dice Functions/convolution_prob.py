# dice probability using recursive discrete convolution

#n = number of dice, k = sum total, f = number of die faces
def conv(n, k, f):
    s = 0
    if n == 1:
        return 1/f
    if n == k:
        return 1/(f**n)
    for j in range(max(1,k-f*(n-1)), min(f+1, k-(n-1)+1)):
        s += conv(n-1, k-j, f) * conv(1, j, f)
    return s
