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
arr1 = sorted(list(map(int, input().split())))
arr2 = sorted(list(map(int, input().split())))
dist1 = []
dist2 = []

for i in range(n):
    if i < n-1:
        dist1.append(arr1[i+1] - arr1[i])
        dist2.append(arr2[i+1] - arr2[i])
    else:
        dist1.append(arr1[0] + 360000 - arr1[i])
        dist2.append(arr2[0] + 360000 - arr2[i])

i = 0
j = 0
f = getfail(dist2)
k = False
key = False
while i < n:
    while j and dist1[i] != dist2[j]:
        j = f[j-1]
    if dist1[i] == dist2[j]:
        if j == n-1:
            key = True
            break
        else:
            j += 1
    i += 1
    if i == n and k == False:
        i -= n
        k = True

if key == True:
    print("possible")
else:
    print("impossible")