K, N = map(int, input().split())

arr = [[] for i in range(K)]

d = 0
for i in range(N):
    arr[0].append(i+1)
for i in range(1,K):
    for j in range(N):
        arr[i].append(1 + N*j + d)       
    d += 1


for i in range(K):
    for j in range(N):
        print(arr[i][j], end= ' ')
    print()