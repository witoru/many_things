N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
arr2 = arr[:]
answer = [-1 for _ in range(N)]

for i in range(N):
    count = 1
    for j in range(N):
        if (arr2[i][0] < arr2[j][0] and arr2[i][1] < arr2[j][1]):
            count += 1
    answer[i] = count

for i in answer:
    print(i, end = " ")