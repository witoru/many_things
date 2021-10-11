def getfail(pattern):
    n = len(pattern)
    f = [0 for i in range(n)]
    begin = 1
    m = 0
    while begin + m < n:
        if pattern[begin + m] == pattern[m]:
            m += 1
            f[begin + m -1] = m
        elif pattern[begin + m] != pattern[m]:
            if m == 0:
                begin += 1
            else:
                begin += m - f[m-1]
                m = f[m-1]
    return f

S = input()
P = input()
f = getfail(P)
S_len = len(S)
P_len = len(P)
i = 0
j = 0
a = 0

while i < S_len:
    while j and S[i] != P[j]:
        j = f[j-1]
    if S[i] == P[j]:
        if j == P_len - 1:
            print(1)
            a = 1
            break
        else:
            j += 1
    i += 1

if a == 0:
    print(0)