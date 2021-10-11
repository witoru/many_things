N, M = map(int, input().split())

arr = [True for _ in range (M+1)]
arr[0] = False
arr[1] = False
i = 2
n = 2

while i < M+1:
    if arr[i] == True:
        while i * n < M + 1:
            arr[i * n] = False
            n += 1
    n = 2
    i += 1

i = N
while i < M+1:
    if arr[i] == True:
        print(i)
    i += 1