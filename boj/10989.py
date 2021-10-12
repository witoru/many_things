import sys
input = sys.stdin.readline
arr = [0 for _ in range(10001)]

N = int(input())

for _ in range(N):
    n = int(input())
    arr[n] += 1

for i in range(1, N+1):
    for _ in range(arr[i]):
        print(i)