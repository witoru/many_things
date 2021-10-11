def getfail(P):
    n = len(P)
    f = [0 for _ in range(n)]
    i = 1
    j = 0
    while i < n:
        while j and P[i] != P[j]:
            j = f[j-1]
        if P[i] == P[j]:
            j += 1
            f[i] = j            
        i += 1
    return f

L = int(input())
S = input()
f = getfail(S)
min = L - f[L-1]

print(min)