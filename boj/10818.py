# https://www.acmicpc.net/problem/10818
N = int(input())
arr = list(map(int, input().split()))
Max = -1000001
Min = 1000001
for i in range(N):
    if arr[i] > Max:
        Max = arr[i]
    if arr[i] < Min:
        Min = arr[i]

print(Min, Max)