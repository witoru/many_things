def getfail(P):
    n = len(P)
    i = 1
    j = 0
    f = [0 for _ in range(n)]
    while i < n:
        while j and P[i] != P[j]:
            j = f[j-1]
        if P[i] == P[j]:
            j += 1
            f[i] = j
        i += 1
    return f

S = input()
P = input()
f = getfail(P)
i = 0
j = 0
count = False
n = len(S)

while i < n:
    if S[i].isdecimal() == False:
        while j and S[i] != P[j]:
            j = f[j-1]
        if S[i] == P[j]:
            if j == len(P) -1:
                print(1)
                count = True
                break
            else:
                j += 1
    i += 1


if count == False:
    print(0)
