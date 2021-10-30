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

n = int(input())
S = input()
f = getfail(S)
i = 0
sum = 0
par1 = 0

while i < n:
    if f[i] > 0:
        min = i+1 - f[i]
        if (i+1)%min != 0:
            par1 = (i+1)%min
        else:
            par1 = min
        while f[par1-1] > 0:
            min = par1 - f[par1-1]
            if par1%min != 0:
                par1 = par1%min
            else:
                par1 = min
        sum += (i + 1 - par1)
    i += 1
    par1 = 0

print(sum)