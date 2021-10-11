# https://www.acmicpc.net/problem/10950
T = int(input())
arr = []
for i in range(T):
    arr.append(list(map(int, input().split())))

for i in range(T):
    print(arr[i][0] + arr[i][1])