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

arr1 = []
arr2 = []
a = 0
b = 0
i = 0
j = 0
arr1.append(input())
while arr1[a] != '.':
    arr1.append(input())
    a += 1

while b < a:
    f = getfail(arr1[b])
    if f[len(arr1[b]) - 1] >= len(arr1[b]) / 2:
        if len(arr1[b]) % (len(arr1[b]) - f[len(arr1[b])-1]) == 0:
            arr2.append(len(arr1[b]) / (len(arr1[b]) - f[len(arr1[b])-1]))
        else: arr2.append(1)
    else:
        arr2.append(1)
    b += 1

for i in arr2:
    print('%d'%(i))