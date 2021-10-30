T = int(input())
arr = []
apt = [list(range(1, 15))]
for i in range(T):
    arr.append([])
    arr[i].append(int(input()))
    arr[i].append(int(input()) - 1)

for i in range(1, 15):
    apt.append([0 for _ in range(14)])
    for j in range(14):
        for h in range(j+1):            
            apt[i][j] += apt[i-1][h]

for ar in arr:
    print(apt[ar[0]][ar[1]])