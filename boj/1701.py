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

str1 = input()
arr1 = []
i = 0
while i < len(str1):
    f = getfail(str1[i:])
    arr1.append(max(f))
    i += 1
print(max(arr1))
