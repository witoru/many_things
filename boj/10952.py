# https://www.acmicpc.net/problem/10952
arr = []
count = 0
while 1:
    arr.append(list(map(int, input().split())))
    if (arr[count][0] == 0) and (arr[count][1] == 0):
        break
    count += 1

for i in range(count):
    print(arr[i][0]+ arr[i][1])