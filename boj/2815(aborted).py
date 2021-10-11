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

S = list(input().rstrip('$').split())
P = list(input().rstrip('$').split())

dic = {}
i = 0
j = 0
f = getfail(P)
S_len = len(S)
P_len = len(P)
bo = False
while i < S_len:
    if not (S[i] in dic):
        if j == P_len-1:
            print(i + 1 - j)
            break
        if P[j] in P[:j]:
            j = f[j-1]
            while j and dic[S[i]] != P[j]:
                j = f[j -1]
            if j < (P_len / 2):
                dic.clear()
                for h in range(j):
                    dic[S[i-j+h]] = P[h]
                if j == 0:
                    dic[S[i]] = P[j]
                    i += 1
                    j += 1
                    continue
        if j != P_len -1:
            dic[S[i]] = P[j]
            j += 1

    else:
        while j and dic[S[i]] != P[j]:
            j = f[j -1]
            bo = True
        if bo == True:
            if j < (P_len / 2):
                dic.clear()
                for h in range(j):
                    dic[S[i-j+h]] = P[h]
                if j == 0:
                    dic[S[i]] = P[j]
                    i += 1
                    j += 1
                    continue
        if dic[S[i]] == P[j]:
            if j == P_len-1:
                print(i + 1 - j)
                break
            else:
                j += 1          
    i += 1
