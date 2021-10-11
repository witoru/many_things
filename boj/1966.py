T = int(input())
Tarr = []
ans = []
count = 0
for i in range(T):
    Tarr.append(list(map(int, input().split())))
    Tarr[i].append(list(map(int, input().split())))

for arr in Tarr:
    Max = max(arr[2])
    while arr[1] != -1:
        if arr[2][0] == Max:
            if arr[1] == 0:
                ans.append(count + 1)
                count = 0
                arr[1] = -1
            else:
                arr[2].pop(0)
                arr[1] -= 1
                count += 1
                Max = max(arr[2])
        else:
            if arr[1] == 0:
                arr[2] = arr[2][1:] + arr[2][:1]
                arr[1] = len(arr[2]) - 1
            else:
                arr[2] = arr[2][1:] + arr[2][:1]
                arr[1] -= 1

for i in ans:
    print(i)
            