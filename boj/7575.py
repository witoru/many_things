def getfail(P):
    i = 1
    j = 0
    n = len(P)
    f = [0 for i in range(n)]
    while i < n:
        while j and P[i] != P[j]:
            j = f[j-1]
        if P[i] == P[j]:
            j += 1
            f[i] = j
        i += 1
    return f

