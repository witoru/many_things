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

def gcd(a, b):
    while b != 0:
        tmp = a % b
        a = b
        b = tmp
    return abs(a)

N = int(input())
arr1 = list(input().split())
arr2 = list(input().split())
f = getfail(arr2)
i = 0
j = 0
k = 0
count = 0
if arr1 == arr2:
    count -= 1
while i < N:
    while j and arr1[i] != arr2[j]:
        j = f[j-1]
    if arr1[i] == arr2[j]:
        if j == N-1:
            count += 1
            j = f[j]
        else:
            j += 1
    i += 1
    if i == N and k == 0:
        i -= N
        k += 1
a = gcd(N, count)

print('%d/%d' %(count / a, N / a))